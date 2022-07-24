"""table route
"""

import string
from flask import render_template, request
from flask_login import login_required
import routes
from database.model.perspective import Perspective
from database.event.perspective_event import get_perspectives, add_perspective, update_perspective, convert_json
from main import logger

@routes.bp.route('/perspective/<int:app_id>', methods=['GET', 'POST'])
@login_required
def perspective_list(app_id: int):
    if request.method == 'POST':
        if request.form:
            id = int(request.form.get('id'))
            name = request.form.get('name')
            detail = request.form.get('detail')
            p = Perspective(id=id, name=name, detail=detail)
            update_perspective(p)
        else:
            perspectives_jsons= convert_json(get_perspectives(app_id))
            return perspectives_jsons
    return render_template('custamized_table.html', title = "Perspective List")
