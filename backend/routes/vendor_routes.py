from flask import Blueprint, request, jsonify
from models.vendor import Vendor
from extensions import db

vendor_bp = Blueprint("vendor", __name__)

@vendor_bp.route("/vendor", methods=["POST"])
def create_vendor():
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "Vendor name required"}), 400

    vendor = Vendor(name=data["name"])
    db.session.add(vendor)
    db.session.commit()

    return jsonify({"message": "Vendor created"}), 200


@vendor_bp.route("/vendor", methods=["GET"])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([
        {"id": v.id, "name": v.name}
        for v in vendors
    ])
