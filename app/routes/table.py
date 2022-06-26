from flask import render_template
import routes
from database.model.person import person

@routes.bp.route("/table")
def table():
    persons: list[person] = person.add_test_person()
    return render_template('html/custamized_table.html', items=persons)
