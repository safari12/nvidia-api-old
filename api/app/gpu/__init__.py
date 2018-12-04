from flask import Blueprint

gpu = Blueprint('gpu', __name__)

from . import error_handlers
from . import views
