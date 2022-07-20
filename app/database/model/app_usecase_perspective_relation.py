"""app usecase perspective relation model
"""

import string
from sqlalchemy import ForeignKey
from main import database

class AppUsecasePerspective(database.db.Model):
    __tablename__ = 'app_usecase_perspective_relation'
    
    app_usecase_perspective_id = database.db.Column(database.db.Integer, primary_key=True)
    app_id = database.db.Column(database.db.Integer, ForeignKey("app.app_id"))
    usecase_id = database.db.Column(database.db.Integer, ForeignKey("usecase.usecase_id"))
    perspective_id = database.db.Column(database.db.Integer, ForeignKey("perspective.perspective_id"))
		