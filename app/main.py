# -*- coding: utf-8 -*-
import os
from time import sleep
from flask import Flask, render_template
from flask_login import LoginManager, UserMixin, login_user
import logging

from database import Database, app_setting
import routes

app = Flask(__name__)
app_setting.set_app_config(app=app)
app.register_blueprint(routes.bp)
database = Database(app=app)

login_manager = LoginManager()
login_manager.init_app(app)

class app_user(UserMixin, database.db.Model):
    id = database.db.Column(database.db.Integer, primary_key=True)
    name = database.db.Column(database.db.String(100), unique = False)
    password = database.db.Column(database.db.String(100), unique = False)
    mail = database.db.Column(database.db.String(100), unique = False)
	
    def __init__(self, name):
        self.name = name

@login_manager.user_loader
def load_user(user_id):
    return app_user.query.get(int(user_id))

def logger(message):
	app.logger.setLevel(logging.INFO)
	app.logger.info(message)

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    