#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
## 1. 题目：两数之和
## 2. 题目地址：https://leetcode-cn.com/problems/two-sum/
## 3. 题目内容
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

## 4. 示例:
```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```
## 5. 分析题目
有可能会有以下的情况需要考虑的：
（1）只有两个数与target相等的情况
（2）有比这个数大的情况
（3）有0与target相加的情况
（4）要考虑负数相加的情况
（5）要考虑到target是负数的情况

## 6. 解决办法
（1）a + b = target，不管正负数，当我有a的时候就一定需要一个人(target-a)
（2）定义target_map，把(target-a)作为key，值为下标，放在target_map中
（3）如果某个数在target_map的key中，即这个值为(target-a)，也就是我们要寻找的b，返回当前b的下标和存放在target_map中a的下标
（4）由于一个数据不能重复使用，因此取出的下标不能相同
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_map = {}
        data_len = len(nums)
        for i in range(data_len):
            data = nums[i]
            if data in target_map and target_map[data] != i:
                return i, target_map[data]
            target_map[target - data] = i
        return None, None
