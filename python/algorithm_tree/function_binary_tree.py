#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


class Node(object):
    def __init__(self, value=0, left=None, right=None):
        self.index = 0
        self.value = value
        self.left = left
        self.right = right

    def set_left(self, node):
        node.index = 2 * self.index + 1
        self.left = node

    def set_right(self, node):
        node.index = 2 * self.index + 2
        self.right = node


def get_full_num_by_layer(layer):
    """
    高度为n的满二叉树，节点数量：
    :param layer:
    :return: node_num
    """
    return (2 ** int(layer)) - 1


def get_layer_by_node_num(node_num):
    """
    知道树的节点数，求树的层数：log2（tree_len+1）
    由于二叉树的节点数：
    node_num = 2^layer-1
    由此可知：
    layer = log2(node_num+1)
    :param node_num: 二叉树节点数
    :return: layer
    """
    return round(math.log2(node_num+1))


def get_leaf_node_num_by_node_num(node_num):
    """
    知道节点数求叶子节点数
    1. 先求出来二叉树的层数layer
    2. 求出来层数为layer-1层的满二叉树的节点数full_num
    3. 用当前节点数减去满二叉树的节点数
    :param node_num: 二叉树节点数
    :return:
    """
    layer = get_layer_by_node_num(node_num)
    full_num = get_full_num_by_layer(layer - 1)
    return node_num - full_num


def get_node_num_by_laer_and_leaf_node(layer, leaf_num):
    """
    知道树的层数和叶子节点数，求树的节点数
    :param layer: 层数，根节点为1
    :param leaf_num:
    :return: node_num
    """
    full_num = get_full_num_by_layer(layer-1)
    return full_num + leaf_num


def get_last_leaf_node(data):
    """
    最后一个叶子节点：tree_data[tree_len-1]
    :param data:
    :return:
    """
    return data[-1]


def check_node_is_leaf_by_node_index(node_num, index):
    layer = get_layer_by_node_num(node_num)
    full_num = get_full_num_by_layer(layer - 1)
    first_leaf_index = full_num
    return False if index < first_leaf_index else True


def print_tree(data):
    i = 0
    step = 0
    data_len = len(data)
    print_data = data[:]
    tree = {}
    while step < data_len:
        step = 2 ** i
        layer_data = print_data[:step]
        if layer_data:
            tree[i] = layer_data
        print_data = print_data[step:]
        i += 1
    return tree


if __name__ == '__main__':
    ll = [1, 3, 5, 5, 1, 7, 5, 8, 6, 4, 7, 3, 8, 9, 5, 6, 3, 4, 2]
    print("len", len(ll))
    print(print_tree(ll))



