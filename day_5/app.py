from flask import Flask

app = Flask(__name__)

import posts

app.register_blueprint(posts.bp)