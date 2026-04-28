from flask import Flask
from app.routes import api
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)

    @app.route("/")
    def home():
        return {
            "message": "ACEest Fitness API running",
            "version": os.getenv("APP_VERSION", "v1")
        }

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)