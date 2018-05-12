import re
from functools import reduce


def re_spilt(data, re_rule):
    # re_rule=r'[\s\/\\\:]'
    result = re.split(re_rule, data)
    if not isinstance(result, list):
        result = [result]
    return result


def check_contain_cn(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def check_ALL_en(check_str):
    check_bool = list(map(lambda x: ord(x) < 127, check_str))
    result = reduce(lambda x, y: x and y, check_bool)
    return result


def case_convert(ch):
    """
    全角转半角
    """
    if ch >= "A" and ch <= "Z":
        return ch.lower()
    else:
        inside_code = ord(ch)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring = chr(inside_code)
        return rstring


def re_get_all(re_rule, data):
    result = re_rule.findall(data)
    try:
        if len(result) == 0:
            return []
        if isinstance(result, list) and isinstance(result[0], tuple):
            result = [x for y in result for x in y if len(x) != 0]
        elif isinstance(result, tuple):
            result = [x for x in result if len(x) != 0]

        return result
    except Exception as e:
        print(e)


def replace_all_dict(dict, data):
    for k, v in dict.items():
        data = data.replace(k, v)
