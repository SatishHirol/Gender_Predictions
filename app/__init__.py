from flask import Flask

def create_app():
    app = Flask(__name__)

    # Add any configurations or extensions here if needed

    from .routes import main
    app.register_blueprint(main)

    return app