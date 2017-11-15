import csv

from autologging import logged

from . import commands
from .models import GPU, Watt, Memory
from .exceptions import GPUError


@logged
def get_gpu_list():
    try:
        data = commands.query()
        gpu_list = []
        reader = csv.reader(data.split("\n"), delimiter=',', skipinitialspace=True)

        get_gpu_list._log.debug('data: {}'.format(data))

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
        get_gpu_list._log.error(e)
        raise GPUError()
