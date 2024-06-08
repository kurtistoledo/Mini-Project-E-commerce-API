from flask import Blueprint, request, jsonify
from models import db, Order, OrderProduct, Product
from datetime import datetime

bp = Blueprint('order', __name__)

@bp.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    order = Order(order_date=datetime.utcnow(), customer_id=data['customer_id'])
    db.session.add(order)
    db.session.commit()
    
    for item in data['products']:
        order_product = OrderProduct(order_id=order.id, product_id=item['product_id'], quantity=item['quantity'])
        db.session.add(order_product)
        product = Product.query.get(item['product_id'])
        product.stock -= item['quantity']
        db.session.commit()

    return jsonify({'id': order.id}), 201

@bp.route('/orders/<int:id>', methods=['GET'])
def retrieve_order(id):
    order = Order.query.get_or_404(id)
    products = [{'product_id': op.product_id, 'quantity': op.quantity} for op in order.products]
    return jsonify({'id': order.id, 'order_date': order.order_date, 'customer_id': order.customer_id, 'products': products})

@bp.route('/orders/<int:id>/cancel', methods=['POST'])
def cancel_order(id):
    order = Order.query.get_or_404(id)
    for item in order.products:
        product = Product.query.get(item.product_id)
        product.stock += item.quantity
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order canceled'})

@bp.route('/orders/<int:id>/total', methods=['GET'])
def calculate_order_total(id):
    order = Order.query.get_or_404(id)
    total_price = sum([op.product.price * op.quantity for op in order.products])
    return jsonify({'order_id': id, 'total_price': total_price})
