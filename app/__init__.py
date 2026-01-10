from flask import Flask, redirect, url_for
import os
from flask_session import Session
from config import Config
from app.models import Setting, Currency
from app.extensions import db, mail, migrate
from flask_babel import Babel, gettext, ngettext, lazy_gettext, _
from flask import request, session, g

def format_currency_filter(amount, currency_code, app):
    """Jinja2 filter to format currency with thousand separators"""
    with app.app_context():
        currency = Currency.query.filter_by(code=currency_code).first()
        if not currency:
            default_currency_code = app.config.get('DEFAULT_CURRENCY', 'IDR')
            currency = Currency.query.filter_by(code=default_currency_code).first()

        if not currency:
            # Fallback if no currency is found at all
            symbol = ''
            position = 'before'
            thousands_separator = ','
            decimal_separator = '.'
        else:
            symbol = currency.symbol
            # These attributes need to be added to the Currency model if they are to be dynamic
            position = 'before' 
            thousands_separator = '.'
            decimal_separator = ','

        # Format the amount with thousands separator
        if amount is None:
            amount = 0
            
        if amount == int(amount):
            # If amount is a whole number, format without decimal places
            formatted_amount = f"{int(amount):,}".replace(',', thousands_separator)
        else:
            # Format with 2 decimal places and thousands separator
            formatted_amount = f"{amount:,.2f}".replace(',', 'THOUSANDS_PLACEHOLDER').replace('.', decimal_separator).replace('THOUSANDS_PLACEHOLDER', thousands_separator)

        if position == 'before':
            return f"{symbol}{formatted_amount}"
        else:
            return f"{formatted_amount} {symbol}"

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    # Initialize session first to ensure it's available for Babel
    sess = Session()
    sess.init_app(app)

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    
    # Language selection function
    def get_locale():
        # Check if user has selected a language in session
        if session.get('language'):
            return session.get('language')
            
        # Check Accept-Language header
        return request.accept_languages.best_match(['en', 'id']) or 'en'
    
    # Initialize Babel for internationalization
    babel = Babel(app, locale_selector=get_locale)
    
    # Add language selection route
    @app.route('/set_language/<lang>')
    def set_language(lang):
        session['language'] = lang
        session.modified = True
        return redirect(request.referrer or url_for('dashboard.index'))

    # The database initialization logic has been moved to a separate CLI command.
    # This prevents the app from trying to re-create tables on every startup.

    def load_settings_from_db(app):
        try:
            for setting in Setting.query.all():
                # Handle type conversion
                if setting.value.isdigit():
                    app.config[setting.key] = int(setting.value)
                elif setting.value.lower() in ['true', 'false']:
                    app.config[setting.key] = setting.value.lower() == 'true'
                else:
                    app.config[setting.key] = setting.value
        except Exception as e:
            # This can happen if the database is not yet initialized
            print(f"Could not load settings from DB: {e}")
    # Load settings from DB at startup
    with app.app_context():
        load_settings_from_db(app)

    # Add currency formatting filter
    @app.template_filter('format_currency')
    def format_currency(amount, currency_code):
        return format_currency_filter(amount, currency_code, app)

    # Make config and locale available in all templates
    @app.context_processor
    def inject_global_vars():
        return dict(
            config=app.config,
            current_locale=get_locale()
        )
    
    # Register blueprints
    from app.routes import dashboard, clients, invoices, settings, recurring_invoices

    app.register_blueprint(dashboard.bp)
    app.register_blueprint(clients.bp)
    app.register_blueprint(invoices.bp)
    app.register_blueprint(settings.bp)
    app.register_blueprint(recurring_invoices.bp)
    
    return app