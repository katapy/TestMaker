"""table_header model
"""

import string
from main import database

class table_header(database.db.Model):
    table_name = database.db.Column(database.db.String(100), primary_key=True)
    column_name = database.db.Column(database.db.String(100), primary_key=True)
    display_name = database.db.Column(database.db.String(100), unique = False)