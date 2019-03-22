# -*- coding: utf-8 -*-
import multiprocessing
import time

from datetime import datetime


class lazy(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val


def concate_list(totallist):
    result = [x for sublist in totallist for x in sublist]
    return result


def mp_map(func, data):
    with multiprocessing.Pool(processes=(multiprocessing.cpu_count() - 1)) as pool:
        result = pool.map(func, data)
        return result


def timestamp():
    return str(int(time.mktime(datetime.now().timetuple())))


def valid_list(__list):
    result = [x for x in __list if x]
    return result


def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:%r took: %2.4f sec' % (f.__name__, te - ts))
        return result

    return timed
