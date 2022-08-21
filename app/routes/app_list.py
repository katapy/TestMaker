"""app route
"""

import string
from flask import render_template, request
from flask_login import login_required
import routes
from database.event.app_event import get_all_app, convert_json

@routes.bp.route("/app", methods=['GET', 'POST'])
@login_required
def app_list():
    if request.method == 'POST':
        app_jsons= convert_json(get_all_app())
        return app_jsons
    else:
        return render_template('custamized_table.html', title = "App List")
