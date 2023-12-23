from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thrivedx:rkFd89W5JuX9S4DRRwK4s@10.10.12.207:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello(): 
        return 'Welcome to PetFax'
    
    from . import pet, fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app
