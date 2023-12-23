from flask import Blueprint, render_template
from . import models
import json

bp = Blueprint(
    'pets',
    __name__,
    url_prefix='/pets',
)

#pets = json.load(open('pets.json'))
#print(pets)

@bp.route('/')
def index():
    pets = models.Pet.query.all()
    return render_template('pets/index.html', title="Our Pets", pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = models.Pet.query.get(id)
    return render_template('pets/show.html', pet=pet)