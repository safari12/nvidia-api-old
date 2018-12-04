import subprocess


def query():
    command = "nvidia-smi --query-gpu" + \
        "fan.speed," + \
        "name," + \
        "power.draw," + \
        "power.limit," + \
        "memory.used," + \
        "memory.total," + \
        "utilization.gpu," + \
        "temperature.gpu " + \
        "--format=csv"

    return subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)

