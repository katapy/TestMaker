"""person table event
"""

import json
import string
from sqlalchemy import text
from database.model.person import person
from database.event.table_header_event import get_disply_name
from main import database

def update_person(id: int, name: string):
	p: person = person.query.filter(text(f"id={id}")).first()
	p.name = name
	database.db.session.commit()

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
		# person_json = dict(id=p.id, name=p.name)
		person_json = dict(\
			id=f"<p id={p.id}> {p.id} </p>", \
			name=f"<input id=\"input_{p.id}\" type=\"text\" name=\"intput\" value={p.name} onchange=\"onChangeInput({p.id})\">")
		persons_json.append(person_json)
	return json.dumps(dict(header=get_headers(), data=persons_json))

def get_headers():
	return dict(id=get_disply_name('person', 'id'),\
		 name=get_disply_name('person', 'name'))
