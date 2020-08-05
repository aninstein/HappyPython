#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给一个股票涨跌区间，计算在哪一天买入，哪一天卖出利润最大
"""


def violence_enumeration(shares):
    """
    暴力枚举法
    遍历所有买入卖出组合，选取其中最大的卖出值
    :param shares: 定义股票开盘数组
    :return:
    """
    buy_day = 0
    sell_day = 0
    max_profit = 0
    data_len = len(shares)
    for i in range(data_len):
        for j in range(i, data_len):
            profit = shares[j] - shares[i]
            if profit > max_profit:
                max_profit = profit
                buy_day = i
                sell_day = j
    return buy_day, sell_day, max_profit


def best_function(shares):
    """
    最优解法
    有时候的那些可以套用的技术相关并不似最好的方法，根据题意，进行分析往往能够找到更合适的方法
    1. 如果我在第N天卖出利润最高，那么我最合适的买入点就是前N-1天的最低1的一天
    2. 只要遍历一次，就能找到区间差最大的11一次
    :param shares: 定义股票开盘数组
    :return:
    """
    bug_day = 0
    sell_day = 0
    max_profit = 0
    data_len = len(shares)
    for i in range(data_len):
        if shares[bug_day] > shares[i]:
            bug_day = i

        profit = shares[i] - shares[bug_day]
        if profit > max_profit:
            max_profit = profit
            sell_day = i
    return bug_day, sell_day, max_profit


def main():
    shares = [10, 2, 9, 4, 5, 1, 8, 7, 10, 25]
    bug_day, sell_day, max_profit = best_function(shares)
    print("在第{0}天(股价：{1})买入，在第{2}天(股价：{3})卖出，能够得到最大利润{4}"
          .format(bug_day+1, shares[bug_day], sell_day+1, shares[sell_day], max_profit))


if __name__ == '__main__':
    main()
