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


if __name__ == '__main__':
    data = [1, 4, 5, 1, 5, 8, 7, 5, 9, 6, 7, 4, 5, 6, 7, 0]
    print(count_sort(data))
