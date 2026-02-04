from flask import Blueprint, request, jsonify
from extensions import db
from models.vendor import Vendor

vendor_bp = Blueprint("vendor", __name__)

@vendor_bp.route("/vendor", methods=["POST"])
def create_vendor():
    data = request.json
    vendor = Vendor(name=data["name"])
    db.session.add(vendor)
    db.session.commit()
    return jsonify({"message": "Vendor created"})

@vendor_bp.route("/vendor", methods=["GET"])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([{"id": v.id, "name": v.name} for v in vendors])
