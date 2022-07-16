# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_login import LoginManager, UserMixin
import logging

from database import Database, app_setting
import routes

app = Flask(__name__)
app_setting.set_app_config(app=app)
app.register_blueprint(routes.bp)
database = Database(app=app)

login_manager = LoginManager()
login_manager.init_app(app)

class AppUser(UserMixin, database.db.Model):
    __tablename__ = 'app_user'

    id = database.db.Column(database.db.Integer, primary_key=True)
    name = database.db.Column(database.db.String(100), unique = False)
    password = database.db.Column(database.db.String(100), unique = False)
    mail = database.db.Column(database.db.String(100), unique = False)
	
    def __init__(self, name):
        self.name = name

@login_manager.user_loader
def load_user(user_id):
    return AppUser.query.get(int(user_id))

def logger(message):
	app.logger.setLevel(logging.INFO)
	app.logger.info(message)

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    