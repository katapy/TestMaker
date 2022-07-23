
from flask import Blueprint

bp = Blueprint('web', __name__, url_prefix="/testmaker")

from . import index
from . import table
from . import login
from . import app_list
from . import perspective_list
from . import usecase_list
