"""login
"""
from flask import render_template, redirect, request, abort, flash, url_for
from flask_login import login_user
import routes
from main import app_user

@routes.bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        user = app_user.query.filter_by(name=name).first()
        # if check_password_hash(user.password, password):
        if user is not None and user.password == password:
            login_user(user)
            return redirect('/testmaker/')
        else:
            return "Login failed"
    else:
        return render_template('login.html')
