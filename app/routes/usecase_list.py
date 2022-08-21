"""app route
"""

import string
from flask import render_template, request
from flask_login import login_required
import routes
from database.event.usecase_event import get_usecase, convert_json
from database.event.perspective_event import get_perspectives, get_usecase_related_perspective
from main import logger

@routes.bp.route("/usecase/<int:id>", methods=['GET', 'POST'])
@login_required
def usecases_list(id: int):
    if request.method == 'POST':
        if request.args.get('perspective') is not None:
            usecases = get_usecase_related_perspective(id, int(request.args.get('perspective')))
            return convert_json(usecases=usecases)
        else:
            return convert_json(get_usecase(id))
    else:
        return render_template('item_list.html', title = "Usecase List")
