#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目标题：剑指 Offer 04. 二维数组中的查找
题目链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

输入：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

输出：
target: 5, 输出true
target: 20， 输出false
"""


class Solution(object):
    # def findNumberIn2DArray(self, matrix, target):
    #     """
    #     python最简单的解法，但是这样速度慢而且不通用
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     if not matrix or not matrix[0]:
    #         return False
    #     for row in matrix:
    #         if target in row:
    #             return True
    #     return False

    def findNumberIn2DArray(self, matrix, target):
        """
        解题方案：
        1. 从[0, col]开始，由于这个值是这一行最大的一个值
        2. 同时向右边和下面进行比较，记录right和down都为0
        3. 如果target比左边的大，right则减1
        4. 如果target比左边的小，down则加1
        5. 如果遇到target相等的值，则return true
        6. 如果左边和下面都比target大了还没有找到相等的，就结束循环
        7. 注意临界值
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        # 对于第一个数字就比target大的，直接false
        if matrix[0][0] > target:
            return False
        elif matrix[0][0] == target:
            return True

        # 小的数据量就直接暴力破解法
        if row < 4 and col < 4:
            for i in range(row):
                for j in range(col):
                    if matrix[i][j] == target:
                        return True
            return False

        # 对于临界数据处理
        if row == 1:
            return bool(target in matrix[0])
        if col == 1:
            for i in range(row):
                if matrix[i][0] == target:
                    return True
            return False

        down, right = 0, col-1
        while down < row and right >= 0:
            num = matrix[down][right]
            if num == target:
                return True
            elif num > target:
                right -= 1
            else:
                down += 1
        return False


if __name__ == '__main__':
    data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print(Solution().findNumberIn2DArray(data, 15))
