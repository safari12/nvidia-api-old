from flask import jsonify

from . import gpu
from .exceptions import GPUError


@gpu.errorhandler(GPUError)
def handle_gpu_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response