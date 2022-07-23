
import string
from flask_login import UserMixin
from sqlalchemy.orm import relation
from main import database

class AppUser(UserMixin, database.db.Model):
    __tablename__ = 'app_user'

    id = database.db.Column(database.db.Integer, primary_key=True)
    name = database.db.Column(database.db.String(100), unique = False)
    password = database.db.Column(database.db.String(100), unique = False)
    mail = database.db.Column(database.db.String(100), unique = False)

    apps = relation("App", secondary="app_user_relation", back_populates="app_users")
	
    def __init__(self, name):
        self.name = name
