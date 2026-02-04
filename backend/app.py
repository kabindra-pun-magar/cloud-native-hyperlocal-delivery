from flask import Flask, jsonify
import os
from extensions import db


def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(BASE_DIR, "instance", "data.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Import models AFTER db
    from models.user import User
    from models.vendor import Vendor
    from models.order import Order

    # Import routes AFTER models
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

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
