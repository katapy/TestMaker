"""perspective model
"""

import string
from main import database
from sqlalchemy.orm import relation


class Perspective(database.db.Model):
    __tablename__ = 'perspective'
    
    perspective_id = database.db.Column(database.db.Integer, primary_key=True)
    perspective_name = database.db.Column(database.db.String(100), unique = False)
    perspective_detail = database.db.Column(database.db.Text, unique = False)
    is_setting = database.db.Column(database.db.Boolean, unique = False)

    usecases = relation("Usecase", secondary="app_usecase_perspective_relation", back_populates="perspectives")
    
    def __init__(self, app_name):
        self.app_name = app_name
		