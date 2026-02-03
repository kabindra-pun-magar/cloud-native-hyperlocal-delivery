from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

# Order Model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    status = db.Column(db.String(50))

# Create DB
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Backend Day 3 Running"

# Create User
@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"})

# Create Order
@app.route("/order", methods=["POST"])
def create_order():
    data = request.json
    order = Order(user_id=data["user_id"], status="CREATED")
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order created"})

# Get Orders
@app.route("/orders")
def get_orders():
    orders = Order.query.all()
    return jsonify([{"id": o.id, "user_id": o.user_id, "status": o.status} for o in orders])

if __name__ == "__main__":
    app.run(debug=True)
