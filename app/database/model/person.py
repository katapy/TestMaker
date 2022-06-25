import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(dirname(abspath(__file__))))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
from main import db

class person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique = False)
	
	def __init__(self, name):
		self.name = name

	"""
	def add_test_person():
		p = person(name="test")
		database.db.session.add(p)
		database.db.session.commit()
		test = person.query.filter_by(name='test').first()
		return test
	"""

# db.create_all()