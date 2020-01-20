# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
Info: 堆排序

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。

堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：
1、大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
2、小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
堆排序的平均时间复杂度为 Ο(nlogn)。
"""
import math


def build_max_heap(arr):
    """
    构建最大堆
    :param arr:
    :return:
    """
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    """
    主函数
    :param arr:
    :param i:
    :return:
    """
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    """
    数组交换
    :param arr:
    :param i:
    :param j:
    :return:
    """
    arr[i], arr[j] = arr[j], arr[i]


def heap_sort(arr):
    """
    堆排序
    :param arr:
    :return:
    """
    global arrLen
    arrLen = len(arr)
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr


if __name__ == '__main__':
    test = [1, 8, 123, 18, 99, 300]
    print("************************************")
    print("*              堆排序              *")
    print("************************************")
    print("源列表：", test)
    result = heap_sort(test)
    print("排序后：", result)
    print("************************************")
    input("按任意键退出...")