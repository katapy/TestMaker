"""person table event
"""

import string
from database.model.person import person
from main import database

def add_test_person():
	p = person(name="test")
	database.db.session.add(p)
	database.databasedb.session.commit()
	test: list[person.person] = person.query.order_by(person.name).all()
	return test

def add_person(name: string):
	p = person(name=name)
	database.db.session.add(p)
	database.db.session.commit()
	test: list[person.person] = person.query.order_by(person.name).all()
	return test

def get_all_person():
	return person.query.order_by(person.name).all()
