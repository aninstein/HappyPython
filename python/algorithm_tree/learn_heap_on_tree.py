#!/usr/bin/env python
# -*- coding: utf-8 -*-


def create_heap():
    """
    1. 一般都用数组来表示堆
    2. i结点的父结点下标就为(i–1)/2
    3. 它的左右子结点下标分别为2∗i+1和2∗i+2，如第0个结点左右子结点下标分别为1和2。
    :return:
    """
    pass


def insert_heap(heap_data):
    pass


def delete_heap(heap_data):
    pass


def adjust_heap():
    pass


def make_heap(data):
    """
    构建堆
    :param data:
    :return:
    """
    if len(data) == 1:
        return data
    elif len(data) == 2:
        return [min(data), max(data)]
    elif len(data) == 3:
        min_data = min(data)
        data.remove(min_data)
        data = [min_data] + data

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        min_adjust_heap_down(data, i)
    return data


def min_adjust_heap_down(data, index):
    """
    调整堆，自顶向下，用于堆化
    :param data:
    :param index:
    :return:
    """
    data_len = len(data)
    temp = data[index]
    child_index = 2 * index + 1
    while child_index < data_len:
        if child_index+1 < data_len and data[child_index + 1] < data[child_index]:
            child_index += 1
        if data[child_index] > temp:
            break
        data[index] = data[child_index]
        index = child_index
        child_index = 2 * index + 1
    data[index] = temp


def min_adjust_heap_up(data, index):
    """
    调整堆，自底向上调整，用于插入堆
    :param data:
    :param index:
    :return:
    """
    temp = data[index]
    child_index = (index - 1) / 2
    while index != 0 and child_index >= 0:
        if data[child_index] < temp:
            break
        data[index] = data[child_index]
        index = child_index
        child_index = (index - 1) / 2
    data[index] = temp
