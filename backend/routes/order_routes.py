from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order

order_bp = Blueprint("order", __name__)

@order_bp.route("/order", methods=["POST"])
def create_order():
    data = request.json

    order = Order(
        user_id=data["user_id"],
        vendor_id=data["vendor_id"],
        item=data["item"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order created"})


@order_bp.route("/order", methods=["GET"])
def get_orders():
    orders = Order.query.all()

    result = []
    for o in orders:
        result.append({
            "id": o.id,
            "user_id": o.user_id,
            "vendor_id": o.vendor_id,
            "item": o.item
        })

    return jsonify(result)
