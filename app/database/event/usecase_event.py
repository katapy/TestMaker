"""perspetive list event
"""

import json
import string
from flask_login import current_user
from sqlalchemy import text, select
from database.model.app_user import AppUser
from database.model.app import App
from database.model.usecase import Usecase
from database.event.table_header_event import get_disply_name
from main import database, logger

def get_usecase(app_id: int):
	user: AppUser = current_user
	app: App = [x for x in user.apps if x.app_id == app_id][0]
	# Exclude dummy usecase.
	usecases: list[Usecase] = [x for x in app.usecases if x.usecase_id > 0]
	return usecases

def convert_json(usecases: list[Usecase]):
	usecases_jsons = []
	for usecase in usecases:
		perspective_list = "<select name='usecase' \
			onchange=\"Redirect(this.options[this.selectedIndex].value)\">"
		perspective_list += f"<option value=sample> Select Usecase </option>"
		for perspective in usecase.perspectives:
			perspective_list += f"<option value='../usecase/{perspective.perspective_id}' > {perspective.perspective_name} </option>"
		perspective_list += "</select>"
		perspective_jsons = dict(\
			id=f"<p id={usecase.usecase_id}> {usecase.usecase_id} </p>", \
			name=f"<input id=\"input_{usecase.usecase_id}\" type=\"text\" name=\"intput\" value=\"{usecase.usecase_name}\" onchange=\"onChangeInput({usecase.usecase_id})\">",\
			perspective=perspective_list)
		usecases_jsons.append(perspective_jsons)
	return json.dumps(dict(header=get_headers(), data=usecases_jsons))

def get_headers():
	return dict(id=get_disply_name('usecase_list', 'id'),\
		name=get_disply_name('usecase_list', 'name'),\
		perspective=get_disply_name('usecase_list', 'perspective'))
