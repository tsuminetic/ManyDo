from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#defining db
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    #securing the app
    app.config['SECRET_KEY'] = 'hfsagkjhasgfjkhas'

    #configuring the db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    
    #initializing the db
    db.init_app(app)


    #importing and registering the blueprints
    from views import views
    from auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')



    from models import User,Note

    #session manager
    login_manager=LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id: str) -> User:
        return User.query.get(int(id))

    #creating the db models
    with app.app_context():
        db.create_all()
        # from models 
        # from models import db as models_db
        # models_db.create_all()
        

    return app