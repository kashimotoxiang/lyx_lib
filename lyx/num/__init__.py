# -*- coding: utf-8 -*-

import collections


class MyError(Exception):
    pass


def argmax(data):
    """
        :param data:
        :return max_num, maxIndex
    """
    if data is None and not isinstance(data, list):
        return
    max_num = data[0]
    maxIndex=0
    for i in range(len(data)):
        if data[i] > max_num:
            max_num = data[i]
            maxIndex = i

    return max_num, maxIndex


def list_count(meta_pool, member=None):
    counter = collections.Counter()
    if member is None:
        for meta in meta_pool:
            counter[meta] = counter[meta] + 1
    elif isinstance(member, str):
        for meta in meta_pool:
            try:
                item = getattr(meta, member)
            except Exception as e:
                print(e)

            counter[item] = counter[item] + 1
    else:
        raise MyError('The type of member must be string!')
    return counter
