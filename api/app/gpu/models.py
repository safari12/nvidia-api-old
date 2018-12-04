class GPU:
    def __init__(self, name, fan_speed, temperature, volatile, watt, memory):
        self.name = name
        self.fan_speed = fan_speed
        self.temperature = temperature
        self.volatile = volatile
        self.watt = watt
        self.memory = memory

    def serialize(self):
        return {
            'name': self.name,
            'fan_speed': self.fan_speed,
            'temperature': self.temperature,
            'volatile': self.volatile,
            'watt': {
                'usage': self.watt.usage,
                'cap': self.watt.cap
            },
            'memory': {
                'used': self.memory.used,
                'max': self.memory.max
            }
        }


class Watt:
    def __init__(self, usage, cap):
        self.usage = usage
        self.cap = cap


class Memory:
    def __init__(self, used, max):
        self.used = used
        self.max = max
