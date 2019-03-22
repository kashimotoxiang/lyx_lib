# -*- coding: utf-8 -*-

import re
import sys
import unicodedata
tbl = {i: ' ' for i in range(sys.maxunicode)
       if unicodedata.category(chr(i)).startswith('P')}


class Safedict(dict):
    def __missing__(self, key):
        return key


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


def check_all_en(check_str):
    check_bool = list(map(lambda x: ord(x) < 127, check_str))
    result = all(check_bool)
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


def replace_all_dict(data, dict):
    for k, v in dict.items():
        data = data.replace(k, v)
    return data


def remove_all(str, remover):
    if remover is not None:
        for item in remover:
            str = str.replace(item, '')
    return str


def count_cn(check_str):
    if check_str is None:
        return 0
    check_bool = list(map(lambda x: u'\u4e00' <= x <= u'\u9fff', check_str))
    true_num = check_bool.count(True)
    return true_num


def count_en(check_str):
    if check_str is None:
        return 0
    check_bool = list(map(lambda x: ord(x) < 127, check_str))
    true_num = check_bool.count(True)
    return true_num


def remove_punctuation(text):
    return text.translate(tbl)


def re_remove(re_rule, data):
    return re_rule.sub('', data)


def isalp(a):
    """
    判断是否为ASCII码
    ord()用于将字符a转换整数
    """
    if (ord(a) < 128):
        return True
    else:
        return False


def separate(i_contents):
    '''
    内容分离
    '''
    flag = 0  # 0-英文；1-中文
    o_contents = ['']
    cn, en = None, None
    for i in range(0, len(i_contents)):
        str = i_contents[i]
        if not isalp(str):
            en = i_contents[:i]
            cn = i_contents[i:]
            break

    return en, cn


def auto_up_down_case(contents, mode):
    '''
    智能大小写转换
    全大写的缩写词保持不变
    一般单词的首字母变成小写
    '''
    # mode = 1中-英; 其他英-中
    if(mode == 1):
        index = 1
    else:
        index = 0

    o_contents = ['']

    try:
        contents = contents.split("\n")
        for line in contents:
            words = line.split("\t")
            if (len(words) != 2):
                continue
            if(mode == 1):
                cn = words[0][::-1]
                en = words[1][::-1]
            else:
                cn = words[1]
                en = words[0]

            first_letter = en[0]
            second_letter = en[1]

            if (is_up_case_and_symbol(first_letter) & ~is_up_case_and_symbol(second_letter)):
                en = en.lower()

            # 文档错误修复
            def _char_detect(str, i, ch):
                if(str[i] == ch):
                    return True
                else:
                    return False

            if(_char_detect(en, -1, '(')):
                en = en[0:-1]
                cn = '(' + cn

            if(_char_detect(en, -1, '-')):
                en = en[0:-1]

            if(_char_detect(en, -1, ':')):
                en = en[0:-1]

            if(_char_detect(cn, 0, '：')):
                cn = cn[1:]

            def csv_foramteor(strs):
                nonlocal o_contents
                for i in strs:
                    o_contents.append(i)
                    # o_contents.append('\t')
                o_contents.append('\n')
                # return o_contents

            csv_foramteor([en, '\t', cn])
            # o_contents.append(tmp)

    except IndexError:
        print("auto_up_down_case NameError")

    return ''.join(o_contents)
