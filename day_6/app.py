# Rename this file app.py to use flask run
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

import posts

@app.route('/')
def index():
    # user logged in logic or force to login page
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(f"Slicing username {request.form.get('username')}")
        print(f"Slicing email {request.form.get('email')}")
        # validate user login
        return redirect('/posts')
    else:
        return render_template('login.html')


app.register_blueprint(posts.bp)