#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


if __name__ == '__main__':
    ll = [6, 1, 5, 9, 9, 7, 2, 3, 5, 4, 1, 5, 3]
    print(ll)
    print(heap_sort(ll))
