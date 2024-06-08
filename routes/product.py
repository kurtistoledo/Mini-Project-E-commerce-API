from flask import Blueprint, request, jsonify
from models import db, Product

bp = Blueprint('product', __name__)

@bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(name=data['name'], price=data['price'], stock=data.get('stock', 0))
    db.session.add(product)
    db.session.commit()
    return jsonify({'id': product.id}), 201

@bp.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'stock': product.stock})

@bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.price = data['price']
    product.stock = data['stock']
    db.session.commit()
    return jsonify({'message': 'Product updated'})

@bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})

@bp.route('/products', methods=['GET'])
def list_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in products])
