
from flask_sqlalchemy import SQLAlchemy

# import app_setting
# from database.model.person import person

class Database:
    db: None
    __is_init: bool = False

    def __init__(self, app):
        self.db = SQLAlchemy(app)
        self.__is_init = True

    """
    def add_test_person(self):
        p = person.person(name="test")
        self.db.session.add(p)
        self.db.session.commit()
        test = person.query.filter_by(name='test').first()
        return test
    """
