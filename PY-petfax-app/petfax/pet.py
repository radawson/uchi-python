from flask import Blueprint, render_template
import json

bp = Blueprint(
    'pets',
    __name__,
    url_prefix='/pets',
)

pets = json.load(open('pets.json'))
#print(pets)

@bp.route('/')
def index():
    return render_template('pets/index.html', title="Our Pets", pets=pets)