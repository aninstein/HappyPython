#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import numpy as np


def create_random_bag_data(things_num, bag_type="01", is_random=True):
    if not is_random:
        return {}

    items = []
    for i in range(things_num):
        if bag_type == "multiple":
            number = random.randint(1, 5)
        elif bag_type == "complete":
            number = 999999
        else:
            number = 1
        items.append({
            "number": number,
            "weight": random.randint(1, 10),
            "value": random.randint(1, 20),
            "name": i
        })
    total_weight = random.randint(25, 45)
    return {
        "items": items,
        "total_weight": total_weight,
        "things_num": things_num
    }


def bag_0and1(data):
    """
    01背包问题
    问题描述：有n件物品和容量为m的背包 给出i件物品的重量以及价值 求解让装入背包的物品重量不超过背包容量 且价值最大 。
    特点:这是最简单的背包问题，特点是每个物品只有一件供你选择放还是不放。
    :param data:
    :return:
    """
    print(data)
    total_weight = data.get("total_weight")
    items = data.get("items")
    number = data.get("things_num")
    print("_two_dim_function: ")
    print(_two_dim_function(items, number, total_weight))
    print("_one_dim_function: ")
    print(_one_dim_function(items, number, total_weight))


def _one_dim_function(data, number, total_weight):
    """
    状态转移方程：
    i：表示第几个物品
    k：表示重量几许
    dp[k] = max(value[i]+dp[k-weight[i]], dp[k])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    dp = np.array([0] * col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        # 这个地方需要是从后面到前面，因为如果从前面到后面的话，会把低层级的j给覆盖掉，
        # https://www.cnblogs.com/qie-wei/p/10160169.html
        # 其实是由于状态转移方程为：dp[k](新值) = max(value[i]+dp[k-weight[i]](旧值), dp[k](旧值))
        # 这个k-weight[i]，如果从前往后数的话，这个值就会被上个值更新为新的值而出现错误
        v = item.get("value")
        w = item.get("weight")
        for j in range(col - 1, w - 1, -1):
            dp[j] = max(dp[j - w] + v, dp[j])
    return dp[total_weight]


def _two_dim_function(data, number, total_weight):
    """
    状态转移方程
    i: 表示第几个物品
    j: 表示背包重量
    dp[i][j] = max(value[i]+dp[i-1][j-weight[i]], dp[i-1][j])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    # dp = [[0] * col for _ in range(row)]
    dp = np.array([0] * (row * col)).reshape(row, col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        v = item.get("value")
        w = item.get("weight")
        for j in range(0, col):
            if j >= w:
                input_val = dp[i - 1][j - w] + v
                noput_val = dp[i - 1][j]
                dp[i][j] = max(input_val, noput_val)
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[number - 1][total_weight]


def bag_complete(data):
    """
    完全背包问题
    问题描述：有n件物品和容量为m的背包 给出i件物品的重量以及价值 求解让装入背包的物品重量不超过背包容量 且价值最大 。
    特点：题干看似与01一样 但它的特点是每个物品可以无限选用。
    :param data:
    :return:
    """
    print(data)
    total_weight = data.get("total_weight")
    items = data.get("items")
    number = data.get("things_num")
    print("_complete_two_dim_k_function: ")
    print(_complete_two_dim_k_function(items, number, total_weight))
    print("_complete_two_dim_function: ")
    print(_complete_two_dim_function(items, number, total_weight))
    print("_complete_one_dim_function: ")
    print(_complete_one_dim_function(items, number, total_weight))


def _complete_two_dim_k_function(data, number, total_weight):
    """
    状态转移方程：
    dp[i][j] = max(dp[i-1][j-k*w[i]] + k*v[i], dp[i-1][j])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    # dp = [[0] * col for _ in range(row)]
    dp = np.array([0] * (row * col)).reshape(row, col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        v = item.get("value")
        w = item.get("weight")
        for j in range(1, col):
            for k in range(1, j + 1):
                if j >= k * w:
                    input_val = dp[i - 1][j - k * w] + k * v
                    noput_val = dp[i - 1][j]
                    dp[i][j] = max(input_val, noput_val)
                else:
                    dp[i][j] = dp[i - 1][j]
                    break  # 如果k * w >= j了这个循环就没必要继续了
    return dp[number - 1][total_weight]


def _complete_two_dim_function(data, number, total_weight):
    """
    时间复杂度优化，去除了k循环
    状态转移方程：
    dp[i][j] = max(dp[i][j-w[i]] + v[i], dp[i-1][j])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    # dp = [[0] * col for _ in range(row)]
    dp = np.array([0] * (row * col)).reshape(row, col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        v = item.get("value")
        w = item.get("weight")
        for j in range(w, col):
            if j >= w:
                input_val = dp[i][j - w] + v
                noput_val = dp[i - 1][j]
                dp[i][j] = max(input_val, noput_val)
            else:
                dp[i][j] = dp[i - 1][j]
                break  # 如果w >= j了这个循环就没必要继续了
    return dp[number - 1][total_weight]


def _complete_one_dim_function(data, number, total_weight):
    """
    状态转移方程：
    i：表示第几个物品
    k：表示重量几许
    dp[k] = max(value[i]+dp[k-weight[i]], dp[k])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    dp = np.array([0] * col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        # 这个地方需要增序列遍历，原因是因为完全背包算法实际上是需要进行自我比对的
        # 也就是说我当前的这一轮可以被重复，也就是说一个物品可以放进去多次
        v = item.get("value")
        w = item.get("weight")
        for j in range(w, col):
            dp[j] = max(dp[j - w] + v, dp[j])
    return dp[total_weight]


def bag_multiple(data):
    """
    多重背包问题
    问题描述：有n件物品和容量为m的背包 给出i件物品的重量以及价值 还有数量 求解让装入背包的物品重量不超过背包容量 且价值最大 。
    特点 ：它与完全背包有类似点 特点是每个物品都有了一定的数量。
    :param data:
    :return:
    """
    print(data)
    total_weight = data.get("total_weight")
    items = data.get("items")
    number = data.get("things_num")
    print("_multiple_two_dim_k_function: ")
    print(_multiple_two_dim_k_function(items, number, total_weight))
    print("_multiple_one_dim_k_function: ")
    print(_multiple_one_dim_k_function(items, number, total_weight))


def _multiple_two_dim_k_function(data, number, total_weight):
    """
    状态转移方程：
    dp[i][j] = max(dp[i-1][j-k*w[i]] + k*v[i], dp[i-1][j]) (0< k && k * w[i] <= j && k <=num[i])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    # dp = [[0] * col for _ in range(row)]
    dp = np.array([0] * (row * col)).reshape(row, col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        v = item.get("value")
        w = item.get("weight")
        num = item.get("number")
        for j in range(w, col):
            dp[i][j] = dp[i - 1][j]
            for k in range(1, num + 1):
                if j >= k * w:
                    input_val = dp[i - 1][j - k * w] + k * v
                    dp[i][j] = max(input_val, dp[i][j])
    return dp[number - 1][total_weight]


def _multiple_one_dim_k_function(data, number, total_weight):
    """
    状态转移方程：
    空间复杂度优化，一维数组实现法
    dp[j] = max(dp[j-k*w[i]] + k*v[i], dp[j]) (0 < k && k * w[i] <= j && k <= num[i])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    # dp = [[0] * col for _ in range(row)]
    dp = np.array([0] * col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        v = item.get("value")
        w = item.get("weight")
        num = item.get("number")
        for j in range(col - 1, w - 1, -1):
            for k in range(1, num + 1):
                if j >= k * w:
                    dp[j] = max(dp[j - k * w] + k * v, dp[j])
    return dp[total_weight]


def _multiple_one_dim_bin_function(data, number, total_weight):
    """
    多重背包算法的二进制优化
    1. 先对数据进行整理
    2. 转化成01背包之后再进行动态规划
    dp[j] = max(dp[j-k*w[i]] + k*v[i], dp[j]) (0 < k && k * w[i] <= j && k <= num[i])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    cnt = 0


if __name__ == '__main__':
    things_number = 10
    print("\nbag_01 >>>>>>>>>>>>")
    data = create_random_bag_data(things_number, bag_type="01")
    bag_0and1(data)

    print("\nbag_complete >>>>>>>>>>>>")
    data = create_random_bag_data(things_number, bag_type="complete")
    bag_complete(data)

    print("\nbag_multiple >>>>>>>>>>>>")
    data = create_random_bag_data(things_number, bag_type="multiple")
    bag_multiple(data)
