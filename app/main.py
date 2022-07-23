# -*- coding: utf-8 -*-
import os

from sqlalchemy import true

from flask import Flask
from flask_login import LoginManager
import logging

from database import Database, app_setting
import routes

app = Flask(__name__)
app_setting.set_app_config(app=app)
app.register_blueprint(routes.bp)
database = Database(app=app)

login_manager = LoginManager()
login_manager.init_app(app)

if database.is_init is not True:
    database.is_init = True
    from database.model.app_user_relation import AppUserRelation
    from database.model.app import App
    from database.model.app_user import AppUser
    from database.model.app_usecase_perspective_relation import AppUsecasePerspective
    from database.model.usecase import Usecase
    from database.model.perspective import Perspective

@login_manager.user_loader
def load_user(user_id):
    return AppUser.query.get(int(user_id))

def logger(message):
	app.logger.setLevel(logging.INFO)
	app.logger.info(message)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    