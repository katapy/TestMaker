"""table route
"""

import string
from flask import render_template, request
from flask_login import login_required
import routes
from database.event.perspective_event import get_perspectives, convert_json
from main import logger

@routes.bp.route('/perspective/<int:id>', methods=['GET', 'POST'])
@login_required
def perspective_list(id: int):
    if request.method == 'POST':
        perspectives_jsons= convert_json(get_perspectives(id))
        logger(perspectives_jsons)
        return perspectives_jsons
    else:
        return render_template('custamized_table.html', title = "Perspective List")
