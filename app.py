from flask import Flask
from extension import db, login_manager
from config import Config
from routes import admin


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from models.user import User
        return User.query.get(int(user_id))

    with app.app_context():
        # Import models
        from models import user, hotel, booking

        # Create tables
        db.create_all()
        print("✅ Database created successfully!")

        # Import and register blueprints
        from routes import auth, main
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(main.main_bp)
        app.register_blueprint(admin.admin_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    print("🚀 Server starting at http://127.0.0.1:5000")
    app.run(debug=True)