from extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))

    amount = db.Column(db.Integer)
