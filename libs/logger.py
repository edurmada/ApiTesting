"""
"""
from datetime import datetime

# Clean log on import
with open("log.txt", "w") as wh:
    pass

def log(msg):
    with open("log.txt", "a") as ah:
        ah.write(msg)
        ah.write("\n")


def log_request(func, *args, **kwargs):
    def aux(*args, **kwargs):
        log("REQUEST: {} - {}".format(args, kwargs))
        result = func(*args, **kwargs)
        log(" > RESPONSE: {}".format(result))
        return result
    return aux

def log_test(func, *args, **kwargs):
    def aux(*args, **kwargs):
        log("\n--- TEST: {}  ({}) ---".format(func.__name__, str(datetime.now())))
        result = func(*args, **kwargs)
        log("--- END ({}) ---\n\n".format(str(datetime.now())))
        return result
    return aux