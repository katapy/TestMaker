"""app route
"""

import string
from flask import render_template, request
from flask_login import login_required
import routes
from database.event.usecase_event import get_usecase, convert_json
from main import logger

@routes.bp.route("/usecase/<int:id>", methods=['GET', 'POST'])
@login_required
def usecases_list(id: int):
    if request.method == 'POST':
        app_jsons= convert_json(get_usecase(id))
        logger(app_jsons)
        return app_jsons
    else:
        return render_template('custamized_table.html', title = "Usecase List")
