from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.models import Client
from app import db

bp = Blueprint('clients', __name__, url_prefix='/clients')

@bp.route('/')
def index():
    search = request.args.get('search', '')
    if search:
        clients = Client.query.filter(
            db.or_(
                Client.name.ilike(f'%{search}%'),
                Client.email.ilike(f'%{search}%'),
                Client.company.ilike(f'%{search}%')
            )
        ).order_by(Client.name).all()
    else:
        clients = Client.query.order_by(Client.name).all()
    
    return render_template('clients/index.html', clients=clients, search=search)

@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        client = Client(
            name=request.form['name'],
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            address=request.form.get('address'),
            company=request.form.get('company')
        )
        
        try:
            db.session.add(client)
            db.session.commit()
            flash('Client created successfully!', 'success')
            return redirect(url_for('clients.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating client: {str(e)}', 'error')
    
    return render_template('clients/form.html', client=None)

@bp.route('/<int:id>')
def view(id):
    client = Client.query.get_or_404(id)
    return render_template('clients/view.html', client=client)

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    client = Client.query.get_or_404(id)
    
    if request.method == 'POST':
        client.name = request.form['name']
        client.email = request.form.get('email')
        client.phone = request.form.get('phone')
        client.address = request.form.get('address')
        client.company = request.form.get('company')
        
        try:
            db.session.commit()
            flash('Client updated successfully!', 'success')
            return redirect(url_for('clients.view', id=client.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating client: {str(e)}', 'error')
    
    return render_template('clients/form.html', client=client)

@bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    client = Client.query.get_or_404(id)
    
    try:
        db.session.delete(client)
        db.session.commit()
        flash('Client deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting client: {str(e)}', 'error')
    
    return redirect(url_for('clients.index'))
