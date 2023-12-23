from flask_sqlalchemy import SQLAlchemy 
import json

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ =  'facts' 
    
    id = db.Column(db.Integer, primary_key = True) 
    submitter = db.Column(db.String(250)) 
    fact = db.Column(db.Text) 
    date = db.Column(db.Date)

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    photo = db.Column(db.String(250))
    fact = db.Column(db.Text)

def seed_db():
    with open('pets.json') as file_handle:
        pets=json.load(file_handle)
        for pet in pets:
            db.session.add(Pet(name=pet['pet_name'], photo=pet['pet_photo'], fact=pet['pet_fact']))
        db.session.commit()