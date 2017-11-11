from . import hello


@hello.route('/')
def index():
    return "Hello World!"
