"""perspetive list event
"""

import json
import string

from flask import render_template
from flask_login import current_user
from sqlalchemy import text, select
from database.model.app_user import AppUser
from database.model.app import App
from database.model.perspective import Perspective
from database.model.usecase import Usecase
from database.event.table_header_event import get_disply_name
from main import database

def get_app(app_id: int) -> App:
	user: AppUser = current_user
	return [x for x in user.apps if x.app_id == app_id][0]

def update_perspective(new_perspective: Perspective):
	user: AppUser = current_user
	# if user.apps
	p: Perspective = Perspective.query.filter(text(f"perspective_id={new_perspective.perspective_id}")).first()
	p.perspective_name = new_perspective.perspective_name
	p.perspective_detail = new_perspective.perspective_detail
	database.db.session.commit()

def add_perspective(app_id: int, new_perspective: Perspective):
	# Insert perspective table.
	database.db.session.add(new_perspective)
	database.db.session.commit() # Return id when commit.
	# Insert app_usecase_perspective_relation table(App-perspective relation.)
	t = text(f'insert into app_usecase_perspective_relation(\
		app_id, usecase_id,perspective_id)values({app_id},0,{new_perspective.perspective_id})')
	database.db.session.execute(t)
	database.db.session.commit()

def get_perspectives(app_id: int):
    app: App = get_app(app_id=app_id)
    return app.perspectives

def get_perspective(perspective_id: int) -> Perspective:
	p: Perspective = Perspective.query.filter(text(f"perspective_id={perspective_id}")).first()
	return p


def get_usecase_related_perspective(app_id: int, perspective_id: int):
	perspectives: list[Perspective] = get_perspectives(app_id=app_id)
	p: Perspective = [x for x in perspectives if x.perspective_id == perspective_id][0]
	return p.usecases

def get_perspective_json(perspective_id: int) -> string:
	p: Perspective = Perspective.query.filter(text(f"perspective_id={perspective_id}")).first()
	if p is None:
		return None
	json_perspective = json.dumps(dict(\
		id=p.perspective_id,\
		item_name=p.perspective_name,\
		detail=p.perspective_detail))
	return json_perspective

def convert_json(perspectives: list[Perspective]) -> str:
	perspectives_jsons = []

	# Register Button(before table)
	before = f"<button onClick=\"SetModalActive(0)\"> New </button>"

	for perspective in perspectives:
		usecase_list = ""
		for usecase in perspective.usecases:
			# Exclude dummy.
			if usecase.usecase_id < 1:
				continue
			usecase_list += json.dumps(dict(
				id = usecase.usecase_id,
				name = usecase.usecase_name
			))
		perspective_jsons = dict(
			id=perspective.perspective_id,
			name=perspective.perspective_name,
			relation=dict(
				usecase=usecase_list
			) 
		)
		perspectives_jsons.append(perspective_jsons)

	return json.dumps(dict(\
		before=before,\
		header=get_headers(),\
		data=perspectives_jsons))

def get_headers():
	return dict(id=get_disply_name('perspective_list', 'id'),\
		name=get_disply_name('perspective_list', 'name'),\
		usecase=get_disply_name('perspective_list', 'usecase'))
