from flask import render_template
import routes

@routes.bp.route("/table")
def table():
    return render_template('html/custamized_table.html')
