
from flask import Blueprint

bp = Blueprint('web', __name__, url_prefix="/testmaker")

from . import index
from . import table
