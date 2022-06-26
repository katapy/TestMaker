"""person model
"""

from main import database

class person(database.db.Model):
	id = database.db.Column(database.db.Integer, primary_key=True)
	name = database.db.Column(database.db.String(100), unique = False)
	
	def __init__(self, name):
		self.name = name

	def add_test_person():
		p = person(name="test")
		database.db.session.add(p)
		database.db.session.commit()
		test: list[person] = person.query.order_by(person.name).all()
		return test

database.db.create_all()