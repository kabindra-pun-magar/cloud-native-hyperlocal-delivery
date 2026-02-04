from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order

order_bp = Blueprint("order", __name__)

@order_bp.route("/order", methods=["POST"])
def create_order():
    data = request.json
    order = Order(item=data["item"])
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order created"})

@order_bp.route("/order", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return jsonify([{"id": o.id, "item": o.item} for o in orders])
