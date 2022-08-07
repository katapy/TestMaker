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
from main import database, logger

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

def get_perspective_json(perspective_id: int) -> string:
	p: Perspective = Perspective.query.filter(text(f"perspective_id={perspective_id}")).first()
	json_perspective = json.dumps(dict(\
		id=p.perspective_id,\
		item_name=p.perspective_name,\
		detail=p.perspective_detail))
	return json_perspective

def convert_json(perspectives: list[Perspective]) -> str:
	perspectives_jsons = []

	# modal window info.
	modals = []
	modals.append(render_template('perspective_modal.html')\
			.replace('$item', "Perspective")
			.replace('$id', "0")\
			.replace('$name', "")\
			.replace('$detail', ""))
	
	# Register Button(before table)
	before = f"<button onClick=\"SetModalActive(0)\"> New </button>"

	for perspective in perspectives:
		usecase_list = "<select name='usecase' \
			onchange=\"Redirect(this.options[this.selectedIndex].value)\">"
		usecase_list += f"<option value=sample> Select Usecase </option>"
		for usecase in perspective.usecases:
			# Exclude dummy.
			if usecase.usecase_id < 1:
				continue
			usecase_list += f"<option value='../usecase/{usecase.usecase_id}' > {usecase.usecase_name} </option>"
		usecase_list += "</select>"
		perspective_jsons = dict(
			id=perspective.perspective_id,
			name=perspective.perspective_name
		)
		perspectives_jsons.append(perspective_jsons)

		# modal window info.
		modals.append(render_template('perspective_modal.html')\
			.replace('$item', "Perspective")
			.replace('$id', f"{perspective.perspective_id}")\
			.replace('$name', perspective.perspective_name)\
			.replace('$detail', perspective.perspective_detail))
	return json.dumps(dict(\
		before=before,\
		header=get_headers(),\
		data=perspectives_jsons, \
		modals=modals))

def get_headers():
	return dict(id=get_disply_name('perspective_list', 'id'),\
		name=get_disply_name('perspective_list', 'name'),\
		usecase=get_disply_name('perspective_list', 'usecase'))
