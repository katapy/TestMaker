"""perspetive list event
"""

import json
import string
from flask_login import current_user
from sqlalchemy import text, select
from database.model.app_user import AppUser
from database.model.app import App
from database.model.perspective import Perspective
from database.event.table_header_event import get_disply_name
from main import database, logger

def get_perspectives(app_id: int):
    user: AppUser = current_user
    app: App = [x for x in user.apps if x.app_id == app_id][0]
    return app.perspectives

def convert_json(perspectives: list[Perspective]):
	perspectives_jsons = []
	for perspective in perspectives:
		perspective_jsons = dict(\
			id=f"<p id={perspective.perspective_id}> {perspective.perspective_id} </p>", \
			name=f"<input id=\"input_{perspective.perspective_id}\" type=\"text\" name=\"intput\" value=\"{perspective.perspective_name}\" onchange=\"onChangeInput({perspective.perspective_id})\">")
		perspectives_jsons.append(perspective_jsons)
	return json.dumps(dict(header=get_headers(), data=perspectives_jsons))

def get_headers():
	return dict(id=get_disply_name('perspevtive_list', 'id'),\
		 name=get_disply_name('perspevtive_list', 'name'))
