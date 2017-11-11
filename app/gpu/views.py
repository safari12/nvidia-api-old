import json

from . import gpu
from .models import GPU, Watt, Memory


@gpu.route('/')
def index():
    gpu_list = []

    for i in range(5):
        gpu_list.append(
            GPU(
                name='Geoforce 1070',
                fan_speed=0.45,
                temperature='45C',
                volatile=0.99,
                watt=Watt(
                    usage=65,
                    cap=124
                ),
                memory=Memory(
                    used='1200MB',
                    max='3400MB'
                )
            )
        )

    return json.dumps(gpu_list, default=lambda o: o.__dict__)
