"""app model
"""

import string
from main import database
from sqlalchemy.orm import relation


class App(database.db.Model):
    __tablename__ = 'app'
    
    app_id = database.db.Column(database.db.Integer, primary_key=True)
    app_name = database.db.Column(database.db.String(100), unique = False)

    app_users = relation("AppUser", secondary="app_user_relation", back_populates="apps")
    perspectives = relation("Perspective", secondary="app_usecase_perspective_relation")
    usecases = relation("Usecase", secondary="app_usecase_perspective_relation")
    
    def __init__(self, app_name):
        self.app_name = app_name
		