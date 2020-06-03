import collections
import itertools


def n_grams(a, n):
    z = [iter(a[i:]) for i in range(n)]
    return zip(*z)


def concate_list(totallist):
    result = [x for sublist in totallist for x in sublist]
    return result
