"""person model
"""

import string
from main import database

class person(database.db.Model):
	id = database.db.Column(database.db.Integer, primary_key=True)
	name = database.db.Column(database.db.String(100), unique = False)
	
	def __init__(self, name):
		self.name = name
		
database.db.create_all()