from flask import render_template
import routes
# from database.model.login_user import login_user
from flask_login import login_required

@routes.bp.route("/")
@login_required
def hello():
    return render_template('index.html')
    