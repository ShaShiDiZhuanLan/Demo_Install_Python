#! -*- coding: utf-8 -*-
"""
Author: ZhenYuSha
Create Time: 2020-1-20
Info:  Python打包示例1，单个文件打包
    “pyinstaller -F(单个可执行文件) 程序源 -n 程序名 -w(去掉控制台窗口，这在GUI界面时非常有用) -i 图标.ico”
    “pyinstaller -F test1/Demo_Test1_Python.py”
"""


def bubble_sort(arr):
    """
    冒泡排序
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    test = [1, 8, 123, 18, 99, 300]
    print("************************************")
    print("*             冒泡排序             *")
    print("************************************")
    print("源列表：", test)
    result = bubble_sort(test)
    print("排序后：", result)
    print("************************************")
    input("按任意键退出...")
