#!/usr/bin/env python
# -*- coding: utf-8 -*-


class HeapNode(object):
    def __init__(self):
        self.val = 0
        self.left_child = None
        self.right_child = None


def make_heap(data):
    """
    构建堆
    1. 一般都用数组来表示堆
    2. i结点的父结点下标就为(i–1)/2
    3. 它的左右子结点下标分别为
        （1）左孩子2∗i+1
        （2）右孩子2∗i+2
        （3）如第0个结点左右子结点下标分别为1和2。
    :param data:
    :return:
    """
    pass


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
    pass


def delete_heap(heap_data):
    """
    我们只能够删除堆顶部额元素，也就是根节点的元素
    1. 删除对顶元素的时候，就会变成两个二叉树
    2. 我们把最后一个叶子节点last移动到root节点
    3. 对last节点进行自顶向下的调整，完成树的调整
    :param heap_data:
    :return:
    """
    pass


def min_adjust_heap_top2down(data, index):
    """
    调整堆，自顶向下，用于堆化数组
    :param data: List[int]
    :param index: 调整第几个节点，一般是从第0个节点开始
    :return:
    """
    if not data:
        return
    data_len = len(data)
    node = data[index]
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    while left_child < data_len:

        # 找左右节点中小的那个进行比较
        if right_child < data_len and data[left_child] < data[right_child]:
            min_child = right_child
        else:
            min_child = left_child

        # 如果没有比当前节点更小的子节点，则返回
        if data[min_child] > node:
            break

        # 交换父子节点
        data[index], data[min_child] = data[min_child], data[index]
        # index指向当前min，继续对子节点进行比较
        index = min_child
        left_child = 2 * index + 1
        right_child = 2 * index + 2

    # 与比较到最后一个节点进行交换
    data[index] = node


def min_adjust_heap_bottom2up(data, index):
    """
    调整堆，自底向上调整，用于插入堆
    :param data: List[int]
    :param index: 调整第几个节点，一般是最后一个节点
    :return:
    """
    if not data:
        return
    node = data[index]
    parent = (index - 1) // 2
    while parent > 0:
        # 如果父节点比当前节点小，则直接返回了
        if data[parent] < node:
            break

        # 交换父子节点
        data[index], data[parent] = data[parent], data[index]

        # 继续向上与父节点比较
        index = parent
        parent = (index - 1) // 2

    # 与比较到最后一个节点进行交换
    data[index] = node


def print_heap(heap_data):
    pass


if __name__ == '__main__':
    pass
