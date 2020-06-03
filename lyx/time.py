import time
from datetime import datetime


def timestamp():
    return str(int(time.mktime(datetime.now().timetuple())))


def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:%r took: %2.4f sec' % (f.__name__, te - ts))
        return result

    return timed
