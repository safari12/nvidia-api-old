class GPUError(Exception):
    status_code = 500

    def __init__(self, payload=None):
        self.payload = payload

    def to_dict(self):
        d = dict(self.payload or ())
        d['message'] = 'GPU Error'

        return d
