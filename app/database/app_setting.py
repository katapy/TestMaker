import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
from setting import POSTGRES_DB, POSTGRES_USER
import string

def set_app_config(app):
    uri: string = f"postgresql://localhost/{POSTGRES_DB}?user={POSTGRES_USER}"
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
