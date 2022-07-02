"""table route
"""

import string
from flask import render_template, request
import routes
from database.model.person import person
from database.event.person_event import add_person, get_all_person, convert_json
from main import logger

@routes.bp.route("/table", methods=['GET', 'POST'])
def table():
    if request.method == 'POST':
        data = request.json
        if 'new_input' in data:
            input_data: string = data['new_input']
            add_person(input_data)
        persons: list[person] = get_all_person()
        persons_json = convert_json(persons=persons)
        logger(persons_json)
        return persons_json
    else:
        return render_template('custamized_table.html')
