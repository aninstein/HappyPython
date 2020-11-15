#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目：移掉K位数字
题目链接：https://leetcode-cn.com/problems/remove-k-digits/

输入示例：
    num = "1432219"
    k = 3

输出示例：
    "1219"

"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if not num:
            return "0"
        if k >= len(num):
            return "0"
        num_len = len(num)
        for i in range(k):
            temp = num
            for j in range(1, len(num)):
                if num[j] < num[j-1]:
                    temp = num[:j-1] + num[j:]
                    break
            else:
                return num[:num_len - k]
            num = temp
        return str(int(num))


"""
# 用栈
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
        
            numStack.append(digit)
        
        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack
        
        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"
"""

if __name__ == '__main__':
    num = "1432219"
    k = 3
    print(Solution().removeKdigits(num, k))

