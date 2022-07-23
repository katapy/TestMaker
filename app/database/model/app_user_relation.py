"""app user relation model
"""

import string
from sqlalchemy import ForeignKey
from main import database

class AppUserRelation(database.db.Model):
    __tablename__ = 'app_user_relation'
    
    app_user_relation_id = database.db.Column(database.db.Integer, primary_key=True)
    user_id = database.db.Column(database.db.Integer, ForeignKey("app_user.id"))
    app_id = database.db.Column(database.db.Integer, ForeignKey("app.app_id"))
		