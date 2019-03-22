# -*- coding: utf-8 -*-

import collections
from functools import lru_cache
__digit_map = {
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '零': 0,
    '壹': 1, '貳': 2, '參': 3, '肆': 4, '伍': 5, '陸': 6, '柒': 7, '捌': 8, '玖': 9, '0': 0,
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    }

__unit_map = {
    '兆': 10 ** 12, '億': 10 ** 8, '萬': 10 ** 4, '仟': 1000, '佰': 100, '拾': 10, '亿': 10 ** 8,
    '万': 10 ** 4, '千': 1000, '百': 100, '十': 10,
    }

__unit_log_map = {
    '兆': 12, '億': 8, '萬': 4, '仟': 3, '佰': 2, '拾': 1, '亿': 8, '万': 4, '千': 3, '百': 2,
    '十': 1,
    }

digit_unit_map = {}
digit_unit_map.update(__digit_map)
digit_unit_map.update(__unit_map)


def is_digit ( ch ):
    return ch in __digit_map


def is_unit ( ch ):
    return ch in __unit_map


def is_digit_unit ( ch ):
    return ch in digit_unit_map


def digit_map ( ch ):
    return __digit_map[ch]


def unit_map ( ch ):
    return __unit_map[ch]


@lru_cache(maxsize = 500)
def cn_num_conv ( num_str ):
    reverse_str = num_str[::-1]
    num = 0
    order = 1
    is_unit = False

    for item in reverse_str:
        if item in __unit_log_map:
            if is_unit:
                order = order * __unit_map[item]
            else:
                order = __unit_map[item]
            is_unit = True
        else:
            num += __digit_map[item] * order
            order *= 10
            is_unit = False

    if is_unit:
        num += order

    return num


class MyError(Exception):
    pass


def argmax ( data ):
    """
        :param data:
        :return max_num, maxIndex
    """
    if data is None and not isinstance(data, list):
        return
    max_num = data[0]
    maxIndex = 0
    for i in range(len(data)):
        if data[i] > max_num:
            max_num = data[i]
            maxIndex = i

    return max_num, maxIndex


def list_count ( meta_pool, member = None ):
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


