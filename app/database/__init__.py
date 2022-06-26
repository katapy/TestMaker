
from flask_sqlalchemy import SQLAlchemy

class Database:
    db: None
    __is_init: bool = False

    def __init__(self, app):
        self.db = SQLAlchemy(app)
        self.__is_init = True
