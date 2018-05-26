# -*- coding: utf-8 -*-
import multiprocessing
import pickle


def concate_list(list):
    result = []
    for element in list:
        result += element
    return result


def mp_map(func, data):
    with multiprocessing.Pool(processes=(multiprocessing.cpu_count() - 1)) as pool:
        result = pool.map(func, data)
        return result


def save_pkl(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_pkl(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def read_all_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        result =[x.strip() for x in f.readlines()]
    return result
