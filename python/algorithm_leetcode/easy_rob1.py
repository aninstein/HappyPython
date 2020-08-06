#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data_len = len(nums)
        if data_len == 1:
            return nums[0]
        elif data_len == 2:
            return max(nums[0], nums[1])
        elif data_len == 3:
            return max(nums[0]+nums[2], nums[1])

        dp = [0] * data_len
        print(dp)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0] + nums[2], nums[1])
        for i in range(3, data_len):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[data_len-1]


if __name__ == '__main__':
    data = [2, 4, 8, 9, 9, 3]
    print(Solution().rob(data))
