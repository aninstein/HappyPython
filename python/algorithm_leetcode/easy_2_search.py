#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
二分查找
"""
from utils.common_function import CountTime


@CountTime()
def two_search(data, num):
    if not data:
        return -1
    data_len = len(data)
    if data_len == 1:
        return 0 if data[0] > num else 1

    start = 0
    end = data_len - 1

    if num > data[end]:
        return end + 1
    elif num < data[start]:
        return start

    index = len(data) // 2
    while end - start > 1:  # 需要超过1，才能继续二分
        data_num = data[index]
        if data_num < num:
            start = index
        elif data_num > num:
            end = index
        else:
            return index

        index = (start + end) // 2

    # 求出的index有可能只是附近的值而不是具体的值，需要校准这个字段在哪个位置
    if index > 1 and data[index-1] < num < data[index]:
        return index - 1
    elif index < data_len - 1 and data[index] < num < data[index+1]:
        return index + 1
    return index


@CountTime()
def each_search(data, num):
    if not data:
        return -1
    data_len = len(data)
    if data_len == 1:
        return 0 if data[0] > num else 1

    for i in range(1, data_len):
        if data[i] > num:
            return i-1
    return data_len


if __name__ == '__main__':
    ll = list(range(10000000))
    print "two_search"
    print two_search(ll, 4815445)

    print "each_search"
    print each_search(ll, 4815445)
