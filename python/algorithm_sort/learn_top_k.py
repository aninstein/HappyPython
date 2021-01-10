#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import heapq
import random
import operator

from algorithm_tree.learn_heap_on_tree import make_heap, min_adjust_heap_top2down
from utils import append_count_map


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
    :param data: 数据集合len(data) > 10000
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
    :param data: len(data) > 10000
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
    :param data: len(data) > 10000
    :param k:
    :return:
    """
    if not data:
        data = create_test_data()

    data_max = max(data)
    data_len = len(data)
    limit_num = data_len // 100  # 一个可控范围的值

    # 生成桶
    key_list = list(range(((data_max + 1) // k) + 1))  # 划定桶的范围，我们取最大值除以k
    bucket = {i: [] for i in key_list}

    # 数据入桶
    for i in data:
        key = i // k
        bucket[key].append(i)

    now_len = k  # 距离k个数据的剩余值
    ret_data = []
    for i in range(len(key_list) - 1, -1, -1):
        now_bucket = bucket[key_list[i]]
        bucket_len = len(now_bucket)
        if now_len >= bucket_len:
            ret_data.extend(now_bucket)
            now_len -= bucket_len

            if now_len == 0:
                return ret_data

            # 如果这个数据在一个可接受的范围内，到下一个bucket数据中去取剩余值
            if now_len < limit_num:
                pre = 0 if i-1 == 0 else i-1
                now_bucket = bucket[key_list[pre]]
                extend_data = sort_cut_top_k(now_bucket, now_len)
                ret_data.extend(extend_data)
                return ret_data
            continue

        # now_len < bucket_len
        extend_data = sort_cut_top_k(now_bucket, now_len)
        ret_data.extend(extend_data)
    return ret_data


def top_k_to_divide(data, k):
    """
    分治法
    :param data:
    :param k:
    :return:
    """
    if not data:
        data = create_test_data()

    return divide_function(data, 0, len(data) - 1, k)


def divide_function(data, left, right, k):
    """
    实际调用的分治法方法
    :param data:
    :param left:
    :param right: 一直是len(data) - 1
    :param k:
    :return:
    """
    if left < right and k < right - left:
        pos = divide_position(data, left, right)
        if k >= (right - pos):
            cut_data = data[left:]
            return sort_cut_top_k(cut_data, k)
        return divide_function(data, pos + 1, right, k)


def divide_position(data, left, right):
    index = data[right]
    i = left - 1
    for j in range(left, right):
        if index > data[j]:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[right] = data[right], data[i + 1]
    return i + 1


def top_k_to_bigmap(data, k):
    """
    使用大hash表处理
    bigmap处理大数据的方法，适用的场景更大一些，比如有1亿数据，需要找出其中的前1000个数据，这时候就需要考虑到进程能够分配多少内存的问题了
    当我有1亿个浮点型数据，大概是0.913GB的数据，这个数据量在我们硬盘中是一个非常大的数据集合
    如果我们只给进程分配1MB的内存，是肯定无法一次把所有数据内容都读取到内存中的
    因此第一个需要做的，应该是把这个数据先拆分成一个个小的文件
    1. 把大量数据拆分成小的文件，尽管文件是小的，但是里面的数据长度还是大于k
        把数据拆分成小的文件算法：
        1）顺序读文件中，对于每个词c，取hash(c)%2000，然后按照该值存到2000个小文件中。这样每个文件大概是500k左右
        2）如果其中的有的文件超过了1M大小，还可以按照类似的方法继续往下分，直到分解得到的小文件的大小都不超过1M
    2. 我们开始对拆分过后的每个文件，进行计数统计
    3. 根据计数结果，取每一个小的文件的前k个数据，把这前k个数据更新到计数map
    4. 遍历N个小文件之后，这个计数map被更新了N次
    5. 遍历这个计数map，取出前k个数据
    :param data: len(data) >> k
    :param k:
    :return:
    """
    pass


###########
# 公用方法 #
###########
def sort_cut_top_k(data, k):
    """
    排序截取前top个
    :param data: len(data) > k
    :param k:
    :return:
    """
    data = sorted(data)
    return data[len(data) - k:]


def cmp_list(list1, list2):
    """
    比对两个乱序的list内的数是否是一样的
    :param list1:
    :param list2:
    :return:
    """
    count_map1 = {}
    count_map2 = {}
    data_len = len(list1)
    if data_len != len(list2):
        return False

    for i in range(data_len):
        append_count_map(count_map1, list1[i])
        append_count_map(count_map2, list2[i])
    return operator.eq(count_map1, count_map2)


if __name__ == '__main__':
    data = create_test_data(number=30)
    print(data)
    k = 8

    heap_res = top_k_to_heap(copy.deepcopy(data), k)
    priority_res = top_k_to_priority_queue(copy.deepcopy(data), k)
    bucket_res = top_k_to_bucket_sort(copy.deepcopy(data), k)
    divide_res = top_k_to_divide(copy.deepcopy(data), k)

    print("heap_res", heap_res)
    print("priority_res", priority_res)
    print("bucket_res", bucket_res)
    print("divide_res", divide_res)

    print("heap_res is", cmp_list(priority_res, heap_res))
    print("bucket_res is", cmp_list(priority_res, bucket_res))
    print("divide_res is", cmp_list(priority_res, divide_res))



