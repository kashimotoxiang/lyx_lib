import collections
import itertools


def n_grams(a, n):
    z = [iter(a[i:]) for i in range(n)]
    return zip(*z)


def counter():
    counter = collections.defaultdict(itertools.count())
    return counter


def subset(data):
    subset = itertools.chain.from_iterable(
        itertools.combinations(data, n) for n in range(len(data) + 1))
    return subset


def concate_list(totallist):
    result = [x for sublist in totallist for x in sublist]
    return result
