# -*- coding: utf-8 -*-
import os
from time import sleep
from flask import Flask, render_template

from database import Database, app_setting
import routes

app = Flask(__name__)
app.register_blueprint(routes.bp)
app_setting.set_app_config(app=app)
sleep(10)
database = Database(app=app)
db = database.db
# database.add_test_person()
# from database.model import person
# database.db.create_all()

class person(database.db.Model):
	id = database.db.Column(database.db.Integer, primary_key=True)
	name = database.db.Column(database.db.String(100), unique = False)
	
	def __init__(self, name):
		self.name = name

database.db.create_all()

p = person(name="test")
database.db.session.add(p)
database.db.session.commit()
test = person.query.filter_by(name='test').first()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    