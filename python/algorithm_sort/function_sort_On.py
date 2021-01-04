#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
时间复杂度为O(n)的排序
"""


def count_sort(data, start=0, end=100):
    """
    计数排序
    :param data:
    :param start: 数据范围起始
    :param end: 数据范围结束
    :return:
    """
    count_list = [0 for i in range(end-start)]
    for i in data:
        count_list[i-start] += 1

    ret_data = []
    for i, count in enumerate(count_list):
        if not count:
            continue
        ret_data.extend([i+start] * count)
    return ret_data


def bucket_sort(data):
    """
    本算法是对浮点数进行排序，此处的放入桶中的方法为对浮点数取整
    """
    if not data:
        return []
    max_num = max(data)
    buf = {i: [] for i in range(int(max_num) + 1)}  # 不能使用[[]]*(max+1)，这样新建的空间中各个[]是共享内存的
    arr_len = len(data)
    for i in range(arr_len):
        num = data[i]
        buf[int(num)].append(num)  # 将相应范围内的数据加入到[]中
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            arr.extend(sorted(buf[i]))  # 这里还需要对一个范围内的数据进行排序，然后再进行输出
    return arr


def radix_sort(data):

    if not data:
        return []
    max_num = max(data)  # 获取当前数列中最大值
    max_digit = len(str(abs(max_num)))  # 获取最大的位数

    dev = 1  # 第几位数，个位数为1，十位数为10···
    mod = 10  # 求余数的除法
    for i in range(max_digit):
        radix_queue = [list() for k in range(mod * 2)]  # 考虑到负数，我们用两倍队列
        for j in range(len(data)):
            radix = int(((data[j] % mod) / dev) + mod)
            radix_queue[radix].append(data[j])

        pos = 0
        for queue in radix_queue:
            for val in queue:
                data[pos] = val
                pos += 1

        dev *= 10
        mod *= 10
    return data


if __name__ == "__main__":
    # count_data = [1, 4, 5, 1, 5, 8, 7, 5, 9, 6, 7, 4, 5, 6, 7, 0]
    # print(count_sort(data))
    # bucket_data = [3.1, 4.2, 3.3, 3.5, 2.2, 2.7, 2.9, 2.1, 1.55, 4.456, 6.12, 5.2, 5.33, 6.0, 2.12]
    # print(bucket_sort(bucket_data))
    radix_data = [58, 14, 5, 16, 78, 2, 123, 158, 753, 32, 1, 9, 5]
    print(radix_sort(radix_data))
