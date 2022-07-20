"""usecase model
"""

import string
from main import database
from sqlalchemy.orm import relation


class Usecase(database.db.Model):
    __tablename__ = 'usecase'
    
    usecase_id = database.db.Column(database.db.Integer, primary_key=True)
    usecase_name = database.db.Column(database.db.String(100), unique = False)
    usecase_detail = database.db.Column(database.db.Text, unique = False)

    perspectives = relation("Perspective", secondary="app_usecase_perspective_relation", back_populates="usecases")
    
    def __init__(self, app_name):
        self.app_name = app_name
		