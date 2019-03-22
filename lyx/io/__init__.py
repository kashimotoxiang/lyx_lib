# -*- coding: utf-8 -*-
import joblib
import pickle
import os
import csv


def save_pkl(obj, name):
    with open(name + '.pkl', 'wb') as f:
        joblib.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
        # joblib.dump(obj, f)


def load_pkl(name):
    with open(name + '.pkl', 'rb') as f:
        return joblib.load(f)


def read_all_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        result = [x.strip() for x in f.readlines()]
    return result


def write_all(data, filepath):
    folder = os.path.dirname(filepath)
    if len(folder) != 0:
        if not os.path.exists(folder):
            os.makedirs(folder)

    with open(filepath, 'w', encoding='utf-8') as f:
        try:
            if isinstance(data, list) or isinstance(data, tuple):
                for item in data:
                    f.write(str(item))
                    f.write('\n')
            else:
                f.write(data)

        except Exception as e:
            print(str(data))
            print(e)


def get_all_file(Folder_Path, filetypes):
    filespath = []
    for dirpath, dirs, files in os.walk(Folder_Path):  # 递归遍历当前目录和所有子目录的文件和目录
        for name in files:  # files保存的是所有的文件名
            if filetypes is None:
                filename = os.path.join(dirpath, name)  # 加上路径，dirpath是遍历时文件对应的路径
                filespath.append(filename)
            else:
                if os.path.splitext(name)[1] in filetypes:
                    filename = os.path.join(dirpath, name)  # 加上路径，dirpath是遍历时文件对应的路径
                    filespath.append(filename)
    return filespath


def write_dict_csv(filepath, content, fieldnames):
    folder = os.path.dirname(filepath)
    if len(folder) != 0:
        if not os.path.exists(folder):
            os.makedirs(folder)
    with open(filepath, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(content)


def write_all_csv(filepath, content, header=None, trans=False):
    folder = os.path.dirname(filepath)
    if len(folder) != 0:
        if not os.path.exists(folder):
            os.makedirs(folder)

    with open(filepath, 'w', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        if header:
            writer.writerow(header)
        if trans:
            writer.writerows(zip(*content))
        else:
            writer.writerows(content)


def read_csv_dict(filename, __fileds=None):
    with open(filename, 'r', encoding='utf-8') as csvFile:
        data = csv.reader(csvFile)
        # Read the column names from the first line of the file
        fields = next(data)

        if __fileds:
            fields = [x for x in __fileds if x in fields]

        result = []
        for row in data:
            item = dict(zip(fields, row))
            result.append(item)
        return result


def read_csv_tuple(filename, __fileds=None, slice=None):
    result = []

    with open(filename, 'r', encoding='utf-8') as csvFile:
        data = csv.reader(csvFile)
        # Read the column names from the first line of the file

        for row in data:
            if slice:
                row = row[slice]
            result.append(row)
    return result
