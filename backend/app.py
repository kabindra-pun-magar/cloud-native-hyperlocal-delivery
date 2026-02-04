import os
from flask import Flask, jsonify
from extensions import db

from routes.user_routes import user_bp
from routes.vendor_routes import vendor_bp
from routes.order_routes import order_bp


def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DB_PATH = os.path.join(BASE_DIR, "instance", "data.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(vendor_bp)
    app.register_blueprint(order_bp)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return jsonify({"status": "API running"})

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
