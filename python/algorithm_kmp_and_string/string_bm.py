#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目1 求一个字符串是否包含另一个字符串，如果包含返回第一个字符下标，不包含返回-1
题目2 求两个字符串的最长公共子串，返回最大公共子串下标，没有返回-1，多个返回第一个
题目3 求两个字符串的最长公共子序列，返回最大公共子序列，没有返回-1
"""


def problem1_bm(a, b):
    a_len = len(a)
    b_len = len(b)
    if a_len == b_len:
        return 0, a_len if a == b else -1, ""
    elif a_len > b_len:
        main_len, sub_len = a_len, b_len
        main_str, sub_str = a, b
    else:
        main_len, sub_len = b_len, a_len
        main_str, sub_str = b, a

    sub_map = {sub_str: ""}
    for i in range(0, main_len-sub_len):
        cut_str = main_str[i:i+sub_len]
        if cut_str in sub_map:
            return i, cut_str
    return -1, ""


if __name__ == '__main__':
    # 题目1
    a1 = "lichangan love zhuangruiying forever!!1314"
    b1 = "forever!"
    print problem1_bm(a1, b1)

    # 题目2
    a2 = "lichangan love zhuangruiying forever!!1314"
    b2 = "li love zhuadataruiying 1314 !! lichangan zhuangruiying forever!"

    # 题目3
    a3 = "lichangan love zhuangruiying forever!!1314"
    b3 = "l1i2c3h4a5n6g7a8n heihei l1o2v3e4 z4r5y6 !1431514"
