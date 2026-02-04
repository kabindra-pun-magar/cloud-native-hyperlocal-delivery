from extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"), nullable=False)

    item = db.Column(db.String(100), nullable=False)

    user = db.relationship("User", backref="orders")
    vendor = db.relationship("Vendor", backref="orders")
