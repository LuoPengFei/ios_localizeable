# coding=utf-8 

"""
检查多语言格式化是否有语法错误
"""

import os
import re

import utils

def filename(filepath):
    return os.path.split(filepath)[1]

def pragram_error(filepath):
    with open(filepath) as f:
        is_mutli_note = False
        fname = filepath.replace(utils.get_project_path(), '')
        for index, line in enumerate(f):
            line = line.strip()

            if '/*' in line:
                is_mutli_note = True
            if '*/' in line:
                is_mutli_note = False
            if is_mutli_note:
                continue

            if len(line) == 0 or line == '*/':
                continue

            if re.findall(r'^/+', line):
                continue

            regx = r'^".*s?"\s*=\s*".*?";$'
            matchs = re.findall(regx, line)
            if not matchs:
                result = fname + ':line[' + str(index) + '] : ' + line
                print(filepath)
                print(result)


def find_from_file(path):
    paths = os.listdir(path)
    for a in paths:
        a_path = os.path.join(path, a)
        if os.path.isdir(a_path):
            find_from_file(a_path)
        elif os.path.isfile(a_path) and os.path.splitext(a_path)[1]=='.strings':
            pragram_error(a_path)

if __name__ == '__main__':
    find_from_file(utils.get_project_path())
    print('已完成')