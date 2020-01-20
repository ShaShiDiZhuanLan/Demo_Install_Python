#! -*- coding: utf-8 -*-
"""
Author: ZhenYuSha
Create Time: 2020-1-20
Info:  Python打包示例2，多个文件打包
    “pyinstaller -F(单个可执行文件) 程序源 -n 程序名 -w(去掉控制台窗口，这在GUI界面时非常有用) -i 图标.ico”
    “pyinstaller -F test2/Demo_Test2_Python.py”
"""
from test2.Demo_bubble_sort import bubble_sort
from test2.Demo_heap_sort import heap_sort


if __name__ == '__main__':
    test1 = [1, 8, 123, 18, 99, 300]
    test2 = test1[:]
    print("************************************")
    print("*             两个排序             *")
    print("************************************")
    print("列表1 id：", id(test1))
    print("列表2 id：", id(test2))
    print("源列表1：", test1)
    print("源列表2：", test2)
    result1 = bubble_sort(test1)
    result2 = heap_sort(test1)
    print("冒泡后：", result1)
    print("堆排后：", result2)
    print("************************************")
    input("按任意键退出...")
