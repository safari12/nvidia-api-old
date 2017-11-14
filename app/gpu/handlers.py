import csv

from . import commands
from .models import GPU, Watt, Memory
from .exceptions import GPUError


def get_gpu_list():
    try:
        data = commands.query()
        gpu_list = []
        reader = csv.reader(data.split("\n"), delimiter=',', skipinitialspace=True)

        for row in reader:
            if any(row):
                gpu_list.append(GPU(
                    fan_speed=int(row[0]),
                    name=row[1],
                    watt=Watt(
                        usage=float(row[2]),
                        cap=float(row[3])
                    ),
                    memory=Memory(
                        used=int(row[4]),
                        max=int(row[5])
                    ),
                    volatile=int(row[6]),
                    temperature=int(row[7])
                ))

        return gpu_list

    except Exception as e:
        print(e)
        raise GPUError()
