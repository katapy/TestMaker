from flask import render_template
import routes

@routes.bp.route("/")
def hello():
    return render_template('html/index.html')
    