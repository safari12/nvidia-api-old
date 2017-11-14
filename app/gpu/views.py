from flask import jsonify

from . import gpu
from .handlers import get_gpu_list


@gpu.route('/')
def index():
    return jsonify([g.serialize() for g in get_gpu_list()])
