from flask import render_template
import routes
from flask_login import login_required

@routes.bp.route("/")
@login_required
def hello():
    return render_template('index.html')
    