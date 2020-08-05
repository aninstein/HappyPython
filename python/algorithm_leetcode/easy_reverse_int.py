#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num_str = str(abs(x))[::-1]
        if len(num_str) > 10 and num_str[0] not in ('1', '2'):
            return 0
        ret_num = int(num_str) * -1 if x < 0 else int(num_str)
        pow_2 = pow(2, 31)
        if -1 * pow_2 <= ret_num <= pow_2 - 1:
            return ret_num
        return 0

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num_str = str(x)
        data_len = len(num_str)
        left_str = num_str[:(data_len // 2) - 1:-1]
        right_str = num_str[:data_len // 2]
        if left_str == right_str or left_str[:-1] == right_str:
            return True
        return False

    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     """
    #     if x < 0:··
    #         return False
    #     num_str = str(x)
    #     num_len = len(num_str)
    #     for i in range(num_len // 2):
    #         if num_str[i] != num_str[num_len - 1 - i]:
    #             return False
    #     return True


if __name__ == '__main__':
    print(Solution().isPalindrome(1513351))

