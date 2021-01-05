#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq
import random

from algorithm_tree.learn_heap_on_tree import make_heap, min_adjust_heap_top2down


def create_test_data(number=10000):
    return [random.randint(1, number) for i in range(number)]


def top_k_to_heap(data, k):
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


def top_k_to_priority_queue(data, k):
    """
    优先队列：优先队列实际上就是堆
    :param data:
    :param k:
    :return:
    """
    if not data:
        data = create_test_data()

    queue = []
    for i in range(k):
        heapq.heappush(queue, data[i])

    for i in range(k, len(data)):
        num = data[i]
        if num < queue[0]:
            continue
        heapq.heappop(queue)
        heapq.heappush(queue, num)
    return queue


def top_k_to_bucket_sort(data, k):
    """
    桶排序
    :param data:
    :param k:
    :return:
    """
    pass


def top_k_to_divide(data, k):
    """
    分治法
    :param data:
    :param k:
    :return:
    """
    pass


def top_k_to_bigmap(data, k):
    """
    使用大hash表处理
    :param data:
    :param k:
    :return:
    """
    pass


if __name__ == '__main__':
    data = create_test_data(number=100)
    print(data)
    print(top_k_to_priority_queue(data, 10))
