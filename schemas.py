from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Customer, CustomerAccount, Product, Order, OrderProduct

class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

class CustomerAccountSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CustomerAccount

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product

class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order

class OrderProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = OrderProduct
