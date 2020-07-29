#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
## 1. 题目：最大的以 1 为边界的正方形（编号：1139）
## 2. 题目地址：https://leetcode-cn.com/problems/largest-1-bordered-square/
## 3. 题目内容
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。
```
示例 1：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9

示例 2：

输入：grid = [[1,1,0,0]]
输出：1



提示：

    1 <= grid.length <= 100
    1 <= grid[0].length <= 100
    grid[i][j] 为 0 或 1

```

## 5. 分析题目
（1）遍历每一个元素
（2）当有一个元素为1的时候，找到对角点的所有为1的值
（3）遍历这些对角点上的值，找到正方形四个角是否为1
（4）确定四个角都为1，再以顺时针的方式遍历每一条边是否都为1

"""


class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len = len(grid)
        col_len = len(grid[0])
        max_grid = 0
        for i in range(row_len):
            for j in range(col_len):
                if max_grid > row_len - 1 + 1:
                    return pow(max_grid, 2)
                if grid[i][j] == 1:
                    r_d_i = i
                    r_d_j = j
                    while r_d_i < row_len and r_d_j < col_len:
                        if not all((grid[r_d_i][r_d_j], grid[i][r_d_j], grid[r_d_i][j])):
                            r_d_i += 1
                            r_d_j += 1
                            continue

                        now = r_d_i - i + 1
                        if now < max_grid:
                            r_d_i += 1
                            r_d_j += 1
                            continue

                        for p in range(now):
                            if not all((grid[i][j+p], grid[i+p][j], grid[r_d_i][j+p], grid[i+p][r_d_j])):
                                break
                        else:
                            max_grid = now if now > max_grid else max_grid

                        r_d_i += 1
                        r_d_j += 1
        return pow(max_grid, 2)


import pprint


if __name__ == '__main__':
    # grid = [[1, 1, 1],
    #         [1, 1, 0],
    #         [1, 1, 1],
    #         [0, 1, 1],
    #         [1, 1, 1]]
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    pprint.pprint(grid)
    print(Solution().largest1BorderedSquare(grid))
