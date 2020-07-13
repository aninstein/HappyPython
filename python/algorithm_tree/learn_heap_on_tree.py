#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_heap(data):
    """
    构建堆
    1. 一般都用数组来表示堆
    2. i结点的父结点下标就为(i–1)/2
    3. 它的左右子结点下标分别为
        （1）做孩子2∗i+1
        （2）又孩子2∗i+2
        （3）如第0个结点左右子结点下标分别为1和2。
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


def insert_heap(heap_data, node):
    """
    插入数据
    1. 先把数据插入到最后一个叶子节点上
    2. 进行自底向上的调整
    3. 直到调到根节点，完成插入
    :param heap_data:
    :param node:
    :return:
    """
    data_len = len(heap_data)
    heap_data.append(node)
    min_adjust_heap_up(heap_data, data_len)


def delete_heap(heap_data):
    """
    我们只能够删除堆顶部额元素，也就是根节点的元素
    1. 删除对顶元素的时候，就会变成两个二叉树
    2. 我们把最后一个叶子节点last移动到root节点
    3. 对last节点进行自顶向下的调整，完成树的调整
    :param heap_data:
    :return:
    """
    data_len = len(heap_data)
    heap_data[0], heap_data[data_len-1] = heap_data[data_len-1], heap_data[0]
    heap_data.pop()  # 弹出最后一个
    min_adjust_heap_down(heap_data, 0)


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


def print_heap(heap_data):
    pass


if __name__ == '__main__':
    pass
