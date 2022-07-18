"""table route
"""

import string
from flask import render_template, request
from flask_login import login_required
import routes
from database.event.app_event import get_all_app, convert_json
from main import logger

@routes.bp.route("/app", methods=['GET', 'POST'])
@login_required
def app_list():
    if request.method == 'POST':
        app_jsons= convert_json(get_all_app())
        logger(app_jsons)
        return app_jsons
    else:
        return render_template('app_list.html')
