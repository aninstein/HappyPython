#!/usr/bin/env python
# -*- coding: utf-8 -*-


def append_count_map(count_map, key):
    """
    计数Map，值是key的计数
    :param count_map: dict
    :param key:
    :return:
    """
    if count_map is None:
        count_map = {key: 1}
        return count_map

    if key in count_map:
        count_map[key] += 1
        return count_map
    count_map[key] = 1
    return count_map


def append_list_map(list_map, key, val):
    """
    列表Map，值是列表型数值的
    :param list_map: dict
    :param key:
    :param val:
    :return:
    """
    if list_map is None:
        list_map = {key: val}
        return list_map

    if key in list_map:
        list_map[key].append(val)
        return list_map
    list_map[key] = [val, ]
    return list_map