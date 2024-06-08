from flask import Blueprint, request, jsonify
from models import db, Customer, CustomerAccount

bp = Blueprint('customer', __name__)

@bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer(name=data['name'], email=data['email'], phone_number=data['phone_number'])
    db.session.add(customer)
    db.session.commit()
    return jsonify({'id': customer.id}), 201

@bp.route('/customers/<int:id>', methods=['GET'])
def read_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify({'id': customer.id, 'name': customer.name, 'email': customer.email, 'phone_number': customer.phone_number})

@bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.get_json()
    customer = Customer.query.get_or_404(id)
    customer.name = data['name']
    customer.email = data['email']
    customer.phone_number = data['phone_number']
    db.session.commit()
    return jsonify({'message': 'Customer updated'})

@bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted'})

@bp.route('/customer_accounts', methods=['POST'])
def create_customer_account():
    data = request.get_json()
    account = CustomerAccount(username=data['username'])
    account.set_password(data['password'])
    account.customer_id = data['customer_id']
    db.session.add(account)
    db.session.commit()
    return jsonify({'id': account.id}), 201

@bp.route('/customer_accounts/<int:id>', methods=['GET'])
def read_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    customer = Customer.query.get(account.customer_id)
    return jsonify({'id': account.id, 'username': account.username, 'customer': {'id': customer.id, 'name': customer.name, 'email': customer.email}})

@bp.route('/customer_accounts/<int:id>', methods=['PUT'])
def update_customer_account(id):
    data = request.get_json()
    account = CustomerAccount.query.get_or_404(id)
    account.username = data['username']
    account.set_password(data['password'])
    db.session.commit()
    return jsonify({'message': 'Account updated'})

@bp.route('/customer_accounts/<int:id>', methods=['DELETE'])
def delete_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    return jsonify({'message': 'Account deleted'})
