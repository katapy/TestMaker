"""table_header model
"""

from main import database

class TableHeader(database.db.Model):
    __tablename__ = 'table_header'

    table_name = database.db.Column(database.db.String(100), primary_key=True)
    column_name = database.db.Column(database.db.String(100), primary_key=True)
    display_name = database.db.Column(database.db.String(100), unique = False)