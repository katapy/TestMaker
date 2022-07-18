
from flask_sqlalchemy import SQLAlchemy

class Database:
    db: None
    is_init: bool = False

    def __init__(self, app):
        self.db = SQLAlchemy(app)
