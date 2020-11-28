#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


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
    if not data:
        return []
    data_len = len(data)
    if data_len == 1:
        return data
    elif data_len == 2:
        return data if data[0] < data[1] else [data[1], data[0]]

    # 超过3长的数据再需要插入
    heap_data = []
    for i in range(data_len):
        heap_data = insert_heap(heap_data, data[i])
    return heap_data


def insert_heap(heap_data, node):
    """
    插入数据
    1. 先把数据插入到最后一个叶子节点上
    2. 进行自底向上的调整
    3. 调整到父节点比当前节点小，或者调到根节点，完成插入
    :param heap_data:
    :param node:
    :return:
    """
    if not heap_data:
        return [node, ]
    data_len = len(heap_data)
    if data_len == 1:
        return [heap_data[0], node] if heap_data[0] < node else [node, heap_data[0]]

    heap_data.append(node)
    last_index = data_len  # (data_len - 1) + 1，这个+1是因为append了node
    min_adjust_heap_bottom2up(heap_data, last_index)
    return heap_data


def pop_heap(heap_data):
    """
    我们只能够删除堆顶部的元素，也就是根节点的元素
    1. 删除对顶元素的时候，就会变成两个二叉树
    2. 把最后一个节点last移动到root节点(一定要用最后一个元素填补root，原因是删除root之后的剩余部分还是保持的堆的特性的，用最后一个值进行调整可以只调整一次)
    3. 对last节点进行自顶向下的调整，完成堆的调整
    :param heap_data:
    :return: top, new_heap
    """
    if not heap_data:
        return None, heap_data
    data_len = len(heap_data)
    if data_len == 1:
        return heap_data[0], []
    elif data_len == 2:
        return heap_data[0], [heap_data[1]]
    elif data_len == 3:
        ret_heap = [heap_data[1], heap_data[2]] if heap_data[1] < heap_data[2] else [heap_data[2], heap_data[1]]
        return heap_data[0], ret_heap

    top = heap_data[0]
    heap_data[0] = heap_data[data_len-1]
    heap_data = heap_data[:-1]
    min_adjust_heap_top2down(heap_data, 0)
    return top, heap_data


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
        if right_child < data_len and data[left_child] > data[right_child]:
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
    while parent >= 0:
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


#######
# 应用 #
#######
def heap_sort(data):
    """
    堆排序，堆排序其实就是不断弹出堆顶元素完成的排序
    :param data:
    :return:
    """
    if not data:
        return []
    ret_data = []
    top, data = pop_heap(data)
    ret_data.append(top)
    while top and data:
        top, data = pop_heap(data)
        ret_data.append(top)
    return ret_data


def no_k_question(data, k):
    """
    前k个问题
    问题描述：当前有100000个数据，求出其中前100大的数据，或者求其中第100大的数据
    1. 如果求前k大，则构造小顶堆
    2. 如果求前k小，则构建大顶堆
    3. 比较堆顶元素，因为堆顶元素就是第k个元素

    本题求解的是第K个大的问题
    :param data: 数据集合
    :param k: k的长度
    :return:
    """
    if not data:
        data = create_test_data()

    # 构建一个长度为k的堆
    heap_data = make_heap(data[:k])

    # 对剩余数据，与堆顶元素比较
    for i in range(k, len(data)):
        num = data[i]
        if num < heap_data[0]:  # 不能等于，因为前k个可能有重复的
            continue
        heap_data[0] = num
        min_adjust_heap_top2down(heap_data, 0)
    return heap_data


def create_test_data():
    number = 100
    return [random.randint(1, number) for i in range(number)]


if __name__ == '__main__':
    # data = [7, 6, 5, 1, 4, 3, 2]
    # heap = make_heap(data)
    # print(heap)
    # print(heap_sort(heap))
    # for i in [8, 9, 0]:
    #     insert_heap(heap, i)
    # print(heap)
    # ret, heap = pop_heap(heap)
    # print("pop node, top: ", ret, " heap data: ", heap)
    # ret, heap = pop_heap(heap)
    # print("pop node, top: ", ret, " heap data: ", heap)

    big_data = create_test_data()
    print("big data: ", big_data)
    print("big data sort: ", sorted(big_data, reverse=True))
    res = no_k_question(big_data, 10)
    print("res data sort: ", sorted(res, reverse=True))
