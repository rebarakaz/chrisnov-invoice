from flask import Blueprint, render_template
from app.models import Invoice, Client
from app import db
from datetime import datetime, timedelta
from sqlalchemy import func

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    # Get statistics
    total_clients = Client.query.count()
    total_invoices = Invoice.query.count()
    
    # Calculate total revenue (paid invoices)
    total_revenue = db.session.query(func.sum(Invoice.total)).filter(
        Invoice.status == 'paid'
    ).scalar() or 0
    
    # Calculate pending amount (sent/unpaid but not paid)
    pending_amount = db.session.query(func.sum(Invoice.total)).filter(
        Invoice.status.in_(['sent', 'unpaid', 'overdue'])
    ).scalar() or 0
    
    # Get recent invoices
    recent_invoices = Invoice.query.order_by(Invoice.created_at.desc()).limit(5).all()
    
    # Check for overdue invoices
    today = datetime.now().date()
    overdue_invoices = Invoice.query.filter(
        Invoice.due_date < today,
        Invoice.status.in_(['draft', 'sent', 'unpaid'])
    ).all()
    
    # Update overdue status
    for invoice in overdue_invoices:
        if invoice.status != 'overdue':
            invoice.status = 'overdue'
    db.session.commit()
    
    # Get counts by status
    draft_count = Invoice.query.filter_by(status='draft').count()
    sent_count = Invoice.query.filter_by(status='sent').count()
    unpaid_count = Invoice.query.filter_by(status='unpaid').count()
    paid_count = Invoice.query.filter_by(status='paid').count()
    overdue_count = Invoice.query.filter_by(status='overdue').count()
    
    return render_template('dashboard/index.html',
                         total_clients=total_clients,
                         total_invoices=total_invoices,
                         total_revenue=total_revenue,
                         pending_amount=pending_amount,
                         recent_invoices=recent_invoices,
                         draft_count=draft_count,
                         sent_count=sent_count,
                         unpaid_count=unpaid_count,
                         paid_count=paid_count,
                         overdue_count=overdue_count)
