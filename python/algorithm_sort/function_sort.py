#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gnome_sort(data):
    """
    地精排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    i = 0
    while i < data_len - 1:

        if data[i] <= data[i+1]:
            i += 1
        else:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
            i -= 1

        if i < 0:
            i += 1

    return data


def bubble_sort(data):
    """
    冒泡排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    for i in range(data_len):
        for j in range(i + 1, data_len):
            if data[i] > data[j]:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
    return list(data)


def select_sort(data):
    """
    选择排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    for i in range(data_len):
        min_flag = i
        for j in range(i + 1, data_len):
            if data[j] < data[min_flag]:
                min_flag = j

        if min_flag != i:
            tmp = data[i]
            data[i] = data[min_flag]
            data[min_flag] = tmp
    return data


def insert_sort(data):
    """
    直接插入排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    for i in range(1, data_len):
        if data[i] < data[i-1]:
            tmp = data[i]
            for j in range(i, -1, -1):
                if j > 0 and tmp < data[j-1]:
                    data[j] = data[j-1]
                else:
                    data[j] = tmp
                    break
    return data


def shell_sort(data):
    """
    希尔排序，插入排序改进版本
    1. 把队列按照步长，分序列先做直接插入
    2. 缩小等分步长做直接插入
    3. 等分步长为1时候停止
    :param data:
    :return:
    """
    if not data:
        return []
    data_len = len(data)
    ll = data_len-1
    step = int(ll // 2)
    while step >= 1:
        for i in range(step, data_len):
            temp = data[i]
            j = i - step
            while j >= 0 and data[j] > temp:
                data[j + step] = data[j]
                j -= step
            data[j+step] = temp
        step //= 2
    return data


def fast_sort(data):
    """
    快速排序
    :param data:
    :return:
    """
    if not data:
        return []


def merge_sort(data):
    """
    归并排序
    :param data:
    :return:
    """
    if not data:
        return []


def heap_sort(data):
    """
    堆排序
    :param data:
    :return:
    """
    if not data:
        return []


if __name__ == '__main__':
    ll = [5, 6, 4, 1, 5, 7, 8, 9, 2, 3]
    print(shell_sort(ll))

