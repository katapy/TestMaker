"""Imposet setting file test.
"""

import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
from setting import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

def test_postgres_db():
    assert POSTGRES_DB != None

def test_postgres_user():
    assert POSTGRES_USER != None

def test_postgres_password():
    assert POSTGRES_PASSWORD != None
