#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq
import random
import operator

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
    1. 先按照当前数据范围进行分桶
    2. 遍历数据，进行数据落桶
    3. 计算每个桶中数据的数量，当第一个桶数据量小于K，继续到下一个桶
    4. 直到加上某一个桶中的数据超过了K值，这时候再对这个桶中的数据进行桶排序，重复1-3的流程
    5. 最后到桶排序的数据量到一个较小的可控范围（100左右）的时候，直接使用其他的比较排序法取得前K个
    :param data:
    :param k:
    :return:
    """
    if not data:
        data = create_test_data()

    data_max = max(data)
    data_len = len(data)
    limit_num = data_len // 100  # 一个可控范围的值
    key_list = list(range(((data_max + 1) // k) + 1))
    bucket = {i: [] for i in key_list}
    for i in data:
        key = i // k
        bucket[key].append(i)

    now_len = k
    ret_data = []
    for i in range(len(key_list) - 1, -1, -1):
        now_bucket = bucket[key_list[i]]
        bucket_len = len(now_bucket)
        if now_len >= bucket_len:
            ret_data.extend(now_bucket)
            now_len -= bucket_len

            if now_len == 0:
                return ret_data

            if now_len < limit_num:  # 到下一个bucket数据中去取值
                pre = 0 if i-1 == 0 else i-1
                now_bucket = bucket[key_list[pre]]
                extend_data = top_k_to_bucket_sort_sort_cut(now_bucket, now_len)
                ret_data.extend(extend_data)
                return ret_data
            continue
        extend_data = top_k_to_bucket_sort_sort_cut(now_bucket, now_len)
        ret_data.extend(extend_data)
        return ret_data


def top_k_to_bucket_sort_sort_cut(data, k):
    data = sorted(data)
    return data[len(data) - k:]


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
    data = create_test_data(number=10000)
    print(data)
    heap_res = top_k_to_heap(data, 100)
    priority_res = top_k_to_priority_queue(data, 100)
    bucket_res = top_k_to_bucket_sort(data, 100)

    heap_sort = sorted(heap_res)
    priority_sort = sorted(priority_res)
    bucket_sort = sorted(bucket_res)

    print("heap_sort", heap_sort)
    print("priority_sort", priority_sort)
    print("bucket_sort", bucket_sort)

    print(operator.eq(priority_sort, bucket_sort))

