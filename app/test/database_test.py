from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from database import app_setting

app = Flask(__name__)

app_setting.set_app_config(app=app)

db = SQLAlchemy(app)

#テーブルの定義
class person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique = False)
	
	def __init__(self,name):
		self.name = name

"""
db.create_all()


while True:
	p = person(name="test")
	db.session.add(p)
	db.session.commit()
"""
