# LeetCode（python）：剑指 Offer 04. 二维数组中的查找
---

### 1. 题目：剑指 Offer 04. 二维数组中的查找
### 2. 题目链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
### 3. 题目内容
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
### 4. 输入输出示例
#### 输入：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

#### 输出：
target: 5, 输出true
target: 20， 输出false

### 5. 题目分析
1. 从[0, col]开始，由于这个值是这一行最大的一个值
2. 同时向右边和下面进行比较，记录right和down都为0
3. 如果target比左边的大，right则减1
4. 如果target比左边的小，down则加1
5. 如果遇到target相等的值，则return true
6. 如果左边和下面都比target大了还没有找到相等的，就结束循环
7. 注意临界值

### 6. python代码
```python
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
```

### 7. 其他解法
1. 暴力法，时间复杂度O(n*m)
2. 由于每一行都是顺序排列的，很容易想到二分查找法，遍历每一行，对美一行进行二分查找，时间复杂读O(n*logn)
