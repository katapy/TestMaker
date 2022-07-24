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

def update_perspective(new_perspective: Perspective):
	user: AppUser = current_user
	# if user.apps
	p: Perspective = Perspective.query.filter(text(f"perspective_id={new_perspective.perspective_id}")).first()
	p.perspective_name = new_perspective.perspective_name
	p.perspective_detail = new_perspective.perspective_detail
	database.db.session.commit()

def add_perspective(new_perspective: Perspective):
	database.db.session.add(new_perspective)
	database.db.session.commit()

def get_perspectives(app_id: int):
    user: AppUser = current_user
    app: App = [x for x in user.apps if x.app_id == app_id][0]
    return app.perspectives

def convert_json(perspectives: list[Perspective]) -> str:
	perspectives_jsons = []
	modals = []
	for perspective in perspectives:
		usecase_list = "<select name='usecase' \
			onchange=\"Redirect(this.options[this.selectedIndex].value)\">"
		usecase_list += f"<option value=sample> Select Usecase </option>"
		for usecase in perspective.usecases:
			usecase_list += f"<option value='../usecase/{usecase.usecase_id}' > {usecase.usecase_name} </option>"
		usecase_list += "</select>"
		perspective_jsons = dict(\
			id=f"<p id={perspective.perspective_id}> {perspective.perspective_id} </p>", \
			name=f"<button onClick=\"SetModalActive({perspective.perspective_id})\">{perspective.perspective_name}</button>",\
			usecase=usecase_list)
		perspectives_jsons.append(perspective_jsons)
		modals.append(render_template('perspective_modal.html', perspective=perspective)\
			.replace('$item', "Perspective")
			.replace('$id', f"{perspective.perspective_id}")\
			.replace('$name', perspective.perspective_name)\
			.replace('$detail', perspective.perspective_detail))
	return json.dumps(dict(\
		header=get_headers(),\
		data=perspectives_jsons, \
		modals=modals))

def get_headers():
	return dict(id=get_disply_name('perspective_list', 'id'),\
		name=get_disply_name('perspective_list', 'name'),\
		usecase=get_disply_name('perspective_list', 'usecase'))
