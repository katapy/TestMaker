# -*- coding: utf-8 -*-
import os
from time import sleep
from flask import Flask, render_template
import logging

from database import Database, app_setting
import routes

app = Flask(__name__)
app.register_blueprint(routes.bp)
app_setting.set_app_config(app=app)
database = Database(app=app)

def logger(message):
	app.logger.setLevel(logging.INFO)
	app.logger.info(message)


if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    