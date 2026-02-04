from flask import Flask, jsonify
from extensions import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

from models.user import User
from models.vendor import Vendor
from models.order import Order

from routes.user_routes import user_bp
from routes.vendor_routes import vendor_bp
from routes.order_routes import order_bp

app.register_blueprint(user_bp)
app.register_blueprint(vendor_bp)
app.register_blueprint(order_bp)

@app.route("/")
def home():
    return jsonify({"status": "API running"})

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
