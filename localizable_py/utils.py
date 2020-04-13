
import sys,os


# excel 存放路径
EXCEL_PATH = "/Users/luopengfei/Desktop/language/localizable_py/test.xlsx"

# 工程路径
PROJECT_PATH = "/Users/luopengfei/Desktop/language/Localizations/"

# 多语言地址 
LOCALIZABLE_PATH = PROJECT_PATH + "Localizations/"

# filename
Localizable_strings = "Localizable.strings"


# 获取当前路径
def get_current_path():
    return os.getcwd()

# 获取上一级路径
def get_supper_path():
    return os.path.abspath(os.path.dirname(os.getcwd()))


def get_excel_path():
    return EXCEL_PATH


def get_project_path():
    return PROJECT_PATH

def get_localizable_path():
    return LOCALIZABLE_PATH
