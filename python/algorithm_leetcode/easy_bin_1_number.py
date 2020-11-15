#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目：剑指 Offer 15. 二进制中1的个数
题目链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/

请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
例如，把 9 表示成二进制是 1001，有 2 位是 1。
因此，如果输入 9，则该函数输出 2。
"""


def get_bin_1_num(num):
    res = 0
    while num > 0:
        res += 1 & num  # 按位与
        num >>= 1
    return res


if __name__ == '__main__':
    print(get_bin_1_num(10))
