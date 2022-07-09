"""table_header table event
"""

import string
from database.model.table_header import table_header
from main import database

def get_disply_name(table_name: string, column_name: string):
    """Get the display name of the table header from RDB.
    """
    return table_header.query\
        .filter(table_header.table_name==table_name,\
            table_header.column_name==column_name)\
        .first().display_name