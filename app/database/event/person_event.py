"""person table event
"""

import json
import string
from database.model.person import person
from main import database, logger

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

def convert_json(persons: list[person]):
	persons_json = []
	for p in persons:
		person_json = dict(id=p.id, name=p.name)
		persons_json.append(person_json)
	return json.dumps(persons_json)
