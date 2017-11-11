class GPU:
    def __init__(self, name, fan_speed, temperature, volatile, watt, memory):
        self.name = name
        self.fan_speed = fan_speed
        self.temperature = temperature
        self.volatile = volatile
        self.watt = watt
        self.memory = memory


class Watt:
    def __init__(self, usage, cap):
        self.usage = usage
        self.cap = cap


class Memory:
    def __init__(self, used, max):
        self.used = used
        self.max = max
