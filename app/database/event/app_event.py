"""app list event
"""

import json
import string
from unittest import result
from sqlalchemy import text, select
from database.model.app import App
from database.model.app_user import AppUser
from database.model.app_user_relation import AppUserRelation
from database.event.table_header_event import get_disply_name
from main import database, logger

def get_all_app():
    # stmt = select(AppUser).filter(AppUser.name == "admin").order_by(AppUser.id)
    # stmt = select(AppUser).filter(AppUser.id == 1).order_by(AppUser.id)
    # result = database.db.session.execute(stmt).all()
    # result = App.query.order_by(App.app_name).all()
    result = App.query.join(AppUserRelation).join(AppUser).all()
    stmt = (
        select(App).
        join(App.app_users).
        join(AppUser.apps)
    )
    # result = database.db.session.execute(stmt).all()
    return result
    # return person.query.order_by(person.name).all()

def convert_json(apps: list[App]):
	apps_json = []
	for app in apps:
		app_json = dict(\
			id=f"<p id={app.app_id}> {app.app_id} </p>", \
			name=f"<input id=\"input_{app.app_id}\" type=\"text\" name=\"intput\" value={app.app_name} onchange=\"onChangeInput({app.app_id})\">")
		apps_json.append(app_json)
	return json.dumps(dict(header=get_headers(), data=apps_json))

def get_headers():
	return dict(id=get_disply_name('person', 'id'),\
		 name=get_disply_name('person', 'name'))
