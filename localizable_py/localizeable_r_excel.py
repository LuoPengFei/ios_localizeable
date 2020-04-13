"""
从Excel读取多语言
"""

import xlrd
import os

import utils

import localizable_error


LOCALIZATION_DICT = {
    "简体":"zh-Hans",
    "繁体":"zh-Hant",
    "英文":"en",
}

SUPPORT_LOCALIZATIIONN = [
    "zh-Hans",
    "zh-Hant",
    "en",
]


def read_excel_xls(path):
    '''
    读取Excel
    '''
    work_book = xlrd.open_workbook(path)
    sheets = work_book.sheet_names()
    worksheet = work_book.sheet_by_name(sheets[0])

    
    for j in range(0, worksheet.ncols):
        name = worksheet.cell_value(0, j)
        for i in range(1, worksheet.nrows): # 逐列逐行读取数据
            base = worksheet.cell_value(i, 0)
            cur = worksheet.cell_value(i, j)
            lan = '"' + base + '"="' + cur + '";\n'
            text_operate(LOCALIZATION_DICT[name] + ".txt", lan)
    
    # 删除读取过的Excel
    # os.remove(path)
    print("Excel读取结束")

def text_operate(name, txt):
    with open(name, 'a') as f :
        f.write(txt)

def write_localizable_strings(path_dict, mode):
    '''
    将Excel多语言写入多语言文件
    '''
    for (key, value) in path_dict.items():
        text = ""
        with open(key+".txt", 'r') as f:
            text = f.read()
            
        os.remove(key+".txt")

        if len(text) > 0:
            with open(value, mode) as f:
                f.write("\n")
                f.write(text)
                print(value + "\t写入成功")

# 增量写入
def write_localizable_strings_add(path_dict):
    write_localizable_strings(path_dict, 'a')

# 覆盖写入
def write_localizable_strings_cover(path_dict):
    write_localizable_strings(path_dict, 'w')