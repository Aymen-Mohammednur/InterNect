from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from interNect.Config import Config
from interNect.temp import create




db = SQLAlchemy()
bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view='users.login' 
# login_manager.login_message_category="info"

mail=Mail()


def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    # with app.app_context():
        # db.drop_all()
        # db.create_all()
        # create(db)
    bcrypt.init_app(app)
    

    # login_manager.init_app(app)
    mail.init_app(app)

    from interNect.intern.routes import intern
    from interNect.company.routes import company
    from interNect.posts.routes import posts
    from interNect.main.routes import main


    app.register_blueprint(company)
    app.register_blueprint(intern)

    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
