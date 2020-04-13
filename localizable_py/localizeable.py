# coding=utf-8

"""
从Excel读取多语言
"""

import localizeable_r_excel
import utils
import localizable_error

SUPPORT_LOCALIZATIIONN = [
    "zh-Hans",
    "zh-Hant",
    "en",
]

def find_localizable_strings():
    '''
    找多语言路径
    '''
    path_dict = {}
    for i in range(0, len(SUPPORT_LOCALIZATIIONN)):
        path_dict[SUPPORT_LOCALIZATIIONN[i]] = utils.get_localizable_path() + SUPPORT_LOCALIZATIIONN[i] + '.lproj/' + utils.Localizable_strings
    return path_dict


if __name__ == '__main__':
    print("开始读取Excel")
    localizeable_r_excel.read_excel_xls(utils.get_excel_path())
    path_dict = find_localizable_strings()
    print("开始写入多语言文件")
    # 追加
    localizeable_r_excel.write_localizable_strings_add(path_dict)
    # 覆盖
    # localizeable_r_excel.write_localizable_strings_cover(path_dict)

    # 检查多语言文件是否有错误
    print("开始检查多语言格式")
    localizable_error.find_from_file(utils.get_project_path())
    print("多语言格式检查结束")

