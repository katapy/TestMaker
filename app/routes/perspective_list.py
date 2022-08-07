"""table route
"""

import string
from flask import render_template, request
from flask_login import login_required
import routes
from database.model.perspective import Perspective
from database.event.perspective_event import get_perspective_json, get_perspectives, add_perspective, update_perspective, convert_json
from main import logger

@routes.bp.route('/perspective/modal/<int:id>', methods=['GET', 'POST'])
@login_required
def modal_window(id: int):
    if request.method == 'POST':
        return get_perspective_json(id)
    else:
        return render_template('perspective_modal.html')


@routes.bp.route('/perspective/<int:app_id>', methods=['GET', 'POST'])
@login_required
def perspective_list(app_id: int):
    if request.method == 'POST':
        if request.form:
            id = int(request.form.get('id'))
            name = request.form.get('name')
            detail = request.form.get('detail')
            p = Perspective(id=id, name=name, detail=detail)
            if id == 0:
                add_perspective(app_id, p)
            else:
                update_perspective(p)
        else:
            perspectives_jsons= convert_json(get_perspectives(app_id))
            return perspectives_jsons
    return render_template('item_list.html', title = "Perspective List")
