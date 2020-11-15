#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目：克隆图
题目连接：https://leetcode-cn.com/problems/clone-graph/
"""
import copy



# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    pre_path = set()
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

    def build_graph(self, node):
        near_map = {}
        new_node = self.get_new_node(node)
        neighbors = []
        for i in node.neighbors:
            near_node = self.get_new_node(i)
            neighbors.append(near_node)
            near_map[i.val] = near_node

        new_node.neighbors = copy.deepcopy(neighbors)

        near_set = set(near_map.keys())
        next_near = list(near_set - self.pre_path)
        if not next_near:
            return
        self.pre_path += near_set
        for i in next_near:
            self.build_graph(i)

    def get_new_node(self, node):
        new_node = Node()
        new_node.val = node.val
        new_node.neighbors = node.neighbors
        return new_node


if __name__ == '__main__':
    ll = [1, 2, 3, 4, 5]
    cc = [1, 2, 6, 7, 8]
    print(set(ll) - set(cc))





