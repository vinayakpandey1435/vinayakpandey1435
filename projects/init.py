from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app= Flask(__name__)


    app.config['SECRET_KEY'] = 'vinayak_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///db.sqlite'


    #db.init_app(app)


    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app

app = create_app()
db = SQLAlchemy(app)
