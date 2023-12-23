from flask import Blueprint, render_template

bp = Blueprint(
    'posts',
    __name__,
    url_prefix='/posts'
)

def get_things():
    return ["a thing", "Another thing", 42, 'an elephant']

@bp.route('/')
def index():
    return render_template(
        'posts.html',
        title = "This is the title",
        things = get_things(),
        button_id = "btn_test"
    )