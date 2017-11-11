from flask import Blueprint

gpu = Blueprint('gpu', __name__)

from . import views
