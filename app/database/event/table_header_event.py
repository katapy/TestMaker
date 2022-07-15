"""table_header table event
"""

import string
from database.model.table_header import TableHeader
from main import database

def get_disply_name(table_name: string, column_name: string):
    """Get the display name of the table header from RDB.
    """
    return TableHeader.query\
        .filter(TableHeader.table_name==table_name,\
            TableHeader.column_name==column_name)\
        .first().display_name