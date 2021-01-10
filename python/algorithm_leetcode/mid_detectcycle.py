#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目： 环形链表 II
题目链接： https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        用哈希表的方式
        :param head:
        :return:
        """
        def detectCycle(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if not head:
                return None
            point_map = {}
            while head is not None:
                key = id(head)
                if key not in point_map:
                    point_map[key] = head
                    head = head.next
                    continue
                return point_map[key]
            return None

    def detect_cycle_slow_fast_point(self, head):
        """
        快慢指针‘
        :param head:
        :return:
        """
        pass


if __name__ == '__main__':
    pass
