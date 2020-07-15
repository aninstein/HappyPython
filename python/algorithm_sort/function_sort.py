#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

from algorithm_tree.learn_heap_on_tree import make_heap


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
    快速排序，创建新列表存放左边和右边
    1. 分治法的思维
    2. 选择当前序列一个主元，最好是中位数
    3. 比主元大的放在左边
    4. 比主元大的放在中间
    5. 与主元相同的放在中间
    6. 对左边和右边进行2~5的操作
    7. 当队列长度小于2的时候退出
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    if data_len < 2:
        return data

    index = int((data_len+1) // 2)

    right = []
    left = []
    same = []
    for i in data:
        if i > data[index]:
            right.append(i)
        elif i < data[index]:
            left.append(i)
        else:
            same.append(i)
    return fast_sort(left) + same + fast_sort(right)


def merge(left_data, right_data):
    left_index, right_index = 0, 0

    # 有可能left_data与right_data长度不一致，因此只排序到有序的位置，因此用“and”
    merge_list = []
    while left_index < len(left_data) and right_index < len(right_data):  # 这个条件里面限定了，当较短的序列结束排序即结束循环
        if left_data[left_index] < right_data[right_index]:
            merge_list.append(left_data[left_index])
            left_index += 1
        else:
            merge_list.append(right_data[right_index])
            right_index += 1

    # 经过上面的排序之后left和right后面的数据变得是有序的，且左边一定大于右边
    merge_list.extend(left_data[left_index:])
    merge_list.extend(right_data[right_index:])
    return merge_list


def merge_sort_recursion(data):
    """
    归并排序，递归法
    :param data:
    :return:
    """
    if not data:
        return []

    if len(data) <= 1:
        return data

    half = len(data) // 2
    left_data = merge_sort_recursion(data[:half])
    right_data = merge_sort_recursion(data[half:])
    return merge(left_data, right_data)


def merge_sort_iteration(data):
    """
    归并排序，迭代法
    与归并法不同，迭代法直接截取不同步长的子序列进行排序
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
    ret_data = []
    heap_data = data[:]
    while True:
        heap_data = make_heap(heap_data)
        ret_data.append(heap_data[0])
        if len(heap_data) == 1:
            break
        heap_data = heap_data[1:]
    return ret_data


def count_sort(data, count_start=0, count_end=100):
    """
    计数排序，是一个不稳定排序，此设计中data的数据范围0-100
    一般用于数据范围比较小的排序，数据内容固定的排序
    1. 划定一个以数据范围生成的列表
    2. 遍历需要排序的数据，插入到对应的数据范围列表中
    3. 从数据列表中拿出数据
    :param data:
    :param count_start: 计数排序的起始
    :param count_end: 计数排序的截止
    :return:
    """
    count_map = {}
    for i in data:
        if not isinstance(i, int):
            continue
        if i < count_start or i > count_end:
            continue
        if i in count_map:
            count_map[i].append(i)
        else:
            count_map[i] = [i, ]

    ret_data = []
    for i in range(count_start, count_end+1):
        row = count_map.get(i)
        if row:
            ret_data.extend(row)
    return ret_data


def radix_sort(data):
    """
    基数排序
    1. 基数排序一般用于对整数数据进行排序
    2. 从个位起对每一个数据进行排序，再到十位、百位、千位进行排序
    3. 按照每一位排序的结果，从对应的数据栈内取出数据，取出数据的顺序就是有序的排序
    4. 考虑到要对负数进行排序，因此扩容一倍，0-9表示复数，10-19表示正数，整个数据+10
    :param data:
    :return:
    """
    # 构建基数map
    minus_base_map = {}  # 负数
    num_base_map = {}  # 正数
    for i in range(10):
        minus_base_map[i] = []
        num_base_map[i+10] = []

    base_num = 10  # 从10位开始进行除法
    valid_data = data[:]
    ret_data = []
    while valid_data:
        tmp_valid_data = []  # 初始化可用数据列表
        tmp_num_map = copy.deepcopy(num_base_map)
        tmp_minus_map = copy.deepcopy(minus_base_map)
        for row in valid_data:
            index = (abs(row) // base_num) % 10
            if abs(row) > base_num:
                tmp_valid_data.append(row)

            if row > 0:  # 正数放进正数的基数队列
                tmp_num_map[index+10].append(row)
            else:  # 负数放进负数的基数队列
                tmp_minus_map[index].append(row)

        base_num *= 10
        valid_data = tmp_valid_data[:]
        ret_data = []
        for i in range(20):
            if i < 10:
                ret_data.extend(tmp_minus_map[-1 * i])
            else:
                ret_data.extend(tmp_num_map[i])
    return ret_data


def bucket_sort(data):
    """
    桶排序
    :param data:
    :return:
    """


if __name__ == '__main__':
    ll = [1, 6, 7, -8, 4, -7, 45, 14, 24, -57, 89, -124, 101, 245, -784, 1024, 1000, 2222, -1001, 12, 524, 500, 100]
    print(ll)
    print(radix_sort(ll))

