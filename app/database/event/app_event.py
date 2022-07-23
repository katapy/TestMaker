"""app list event
"""

import json
import string
from flask_login import current_user
from sqlalchemy import text, select
from database.model.app import App
from database.model.app_user import AppUser
from database.event.table_header_event import get_disply_name
from main import database, logger

def get_all_app():
    # result = App.query.join(AppUserRelation).join(AppUser).filter(AppUser.name == "admin").all()
    user: AppUser = current_user
    return user.apps


def convert_json(apps: list[App]):
	apps_json = []
	for app in apps:
		app_json = dict(\
			id=f"<p id={app.app_id}> {app.app_id} </p>", \
			name=f"<input id=\"input_{app.app_id}\" type=\"text\" name=\"intput\" value={app.app_name} onchange=\"onChangeInput({app.app_id})\">", \
			perspective=f"<button type=\"button\" onclick=\"Redirect('perspective/{app.app_id}')\"> perspective </button>")
		apps_json.append(app_json)
	return json.dumps(dict(header=get_headers(), data=apps_json))

def get_headers():
	return dict(id=get_disply_name('app_list', 'id'),\
		name=get_disply_name('app_list', 'name'),\
		perspective=get_disply_name('app_list', 'perspective'))
