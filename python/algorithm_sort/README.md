# 排序算法
---

---
## 1. 地精排序
地精排序虽然只有一层循环，但是由于序列内部元素不断的交换比对，时间复杂度依旧是O(n^2)
请直接看代码
```python
def gnome_sort(data):
    """
    地精排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    i = 0
    while i < data_len - 1:

        if data[i] <= data[i+1]:
            i += 1
        else:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
            i -= 1

        if i < 0:
            i += 1

    return data
```
## 2. 冒泡排序
请直接看代码
```python
def bubble_sort(data):
    """
    冒泡排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    for i in range(data_len):
        for j in range(i + 1, data_len):
            if data[i] > data[j]:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
    return list(data)
```
## 3. 选择排序
请直接看代码
```python
def select_sort(data):
    """
    选择排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    for i in range(data_len):
        min_flag = i
        for j in range(i + 1, data_len):
            if data[j] < data[min_flag]:
                min_flag = j

        if min_flag != i:
            tmp = data[i]
            data[i] = data[min_flag]
            data[min_flag] = tmp
    return data
```
## 4. 插入排序
请直接看代码
```python
def insert_sort(data):
    """
    直接插入排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    for i in range(1, data_len):
        if data[i] < data[i-1]:
            tmp = data[i]
            for j in range(i, -1, -1):
                if j > 0 and tmp < data[j-1]:
                    data[j] = data[j-1]
                else:
                    data[j] = tmp
                    break
    return data
```
## 5. 希尔排序
希尔排序，插入排序改进版本，分组进行的插入排序
-    1. 把队列按照步长，分序列先做直接插入
-    2. 缩小等分步长做直接插入
-    3. 等分步长为1时候停止

请直接看代码：
```python
def shell_sort(data):
    """
    希尔排序，插入排序改进版本
    :param data:
    :return:
    """
    if not data:
        return []
    data_len = len(data)
    ll = data_len-1
    step = int(ll // 2)
    while step >= 1:
        for i in range(step, data_len):
            temp = data[i]
            j = i - step
            while j >= 0 and data[j] > temp:
                data[j + step] = data[j]
                j -= step
            data[j+step] = temp
        step //= 2
    return data
```
## 6. 快速排序
快速排序，创建新列表存放左边和右边
-    1. 分治法的思维
-    2. 选择当前序列一个主元，最好是中位数
-    3. 比主元大的放在左边
-    4. 比主元大的放在中间
-    5. 与主元相同的放在中间
-    6. 对左边和右边进行2~5的操作
-    7. 当队列长度小于2的时候退出

请直接看代码：
```python
def fast_sort(data):
    """*
    快速排序
    :param data:
    :return:
    """
    if not data:
        return []

    data_len = len(data)
    if data_len < 2:
        return data

    index = int((data_len+1) // 2)

    right = []
    left = []
    same = []
    for i in data:
        if i > data[index]:
            right.append(i)
        elif i < data[index]:
            left.append(i)
        else:
            same.append(i)
    return fast_sort(left) + same + fast_sort(right)
```

## 7. 归并排序
### （1）归并算法
首先需要明白归并算法，当我们有两个有序序列，arr1与arr2：
```python
arr1 = [1, 2, 4, 7]
arr2 = [2, 2, 3, 5, 9]
```
因为是有序数列，所以我们实际上只需要把某一个序列合入到另一个序列中即可，定义两个下标变量：
```python
left_index, right_index = 0, 0
```
我们一般把长度短的序列合并到长度长的序列中，因此需要把arr1合并到arr2中，定义一个新序列存放合并后的结果
```python
merge_list = []
while left_index < len(left_data) and right_index < len(right_data):  # 这个条件里面限定了，当较短的序列结束排序即结束循环
	if left_data[left_index] < right_data[right_index]:
		merge_list.append(left_data[left_index])
		left_index += 1
	else:
		merge_list.append(right_data[right_index])
		right_index += 1
```
由于我们创建了一个新队列去存合并后的数据，又因为我们只进行了短的队列向长的队列的合并，因此需要把长队列剩余部分的内容，合并到新的队列去
```
merge_list.extend(left_data[left_index:])
merge_list.extend(right_data[right_index:])
```
### （2）归并排序
有了上面归并算法的支持，进行归并排序的时候主要是把当前序列先划分为小的子序列，然后对子序列进行归并，归并后的子序列再进行归并，直到全部序列有序
```python
def merge_sort_recursion(data):
    """
    归并排序，递归法
    :param data:
    :return:
    """
    if not data:
        return []

    if len(data) <= 1:
        return data

    half = len(data) // 2
    left_data = merge_sort_recursion(data[:half])
    right_data = merge_sort_recursion(data[half:])
    return merge(left_data, right_data) 
```


## 8. 堆排序
### （1）堆
1. 一般都用数组来表示堆
2. i结点的父结点下标就为(i–1)/2
3. 它的左右子结点下标分别为
    - 左孩子2∗i+1
    - 右孩子2∗i+2
    - 如第0个结点左右子结点下标分别为1和2
4. 由此可得，如果向上追溯父节点，当节点i的父节点则为：
    - parent = is_int{(child-1) / 2, (child-2) / 2}  
### （2）堆化
由于我们一般用数组存储堆，因此我们先对无序数组进行堆化，堆化两种写法，而且都是自顶向下才能完全的堆化
#### 方法1
```python
def heapify(arr):
    n = len(arr)
    for i in reversed(range(n // 2)):
        shiftDown(arr,n,i)

def shiftDown(arr, n, k):
    while 2 * k + 1 < n:
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] < arr[j]:
            j += 1
        if arr[k] <= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j
```

#### 方法2
```python
def shiftDown2(arr, n, k):
    smallest, l, r = k, 2 * k + 1, 2 * k + 2
    while l < n:
        if arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if smallest == k:
            break
        else:
            arr[k], arr[smallest] = arr[smallest], arr[k]
            k = smallest
            l, r = 2 * k + 1, 2 * k + 2
```

### （3）堆排序
使用堆化方法进行排序
1. 我们每一次堆化都能够得到当前的最大值
2. 这时候用这个最大值存放到新的队列，或者与队列的末尾元素进行交换
3. 剩下的数据继续的进行对花
```python
def heapSort(arr):
    n=len(arr)
    heapify(arr)
    print("堆化：",arr)
    for i in range(n-1):
        arr[n-i-1],arr[0] = arr[0],arr[n-i-1]
        # print("交换最小值后：",arr)
        shiftDown(arr,n-i-1,0)
        # print("调整后：",arr)
```
## 9. 计数排序
计数排序，顾名思义，这个排序的主要作用并不是排序，而是进行计数。
计数排序用于**数据量内容固定，且数据范围较小**的情况，对需要排序的数列进行计数；比如对学生考试分数进行排序，分数值是一个固定的范围0-100，且数据范围不大，则可以使用计数排序。
计数排序步骤：
1. 如果数据内容是正整数，则可以创建一个数组，如果是其他类型的数据，则可以创建一个map
2. 遍历需要排序的数据，按照下标或者map的key，计算同一个数据出现的次数
3. 遍历数组或者map，按照排序结果生成数据

```python
def count_sort(data, start=0, end=100):
    """
    计数排序
    :param data:
    :param start: 数据范围起始
    :param end: 数据范围结束
    :return:
    """
    count_list = [0 for i in range(end-start)]
    for i in data:
        count_list[i-start] += 1

    ret_data = []
    for i, count in enumerate(count_list):
        if not count:
            continue
        ret_data.extend([i+start] * count)
    return ret_data
```
输出结果：
```linux
input: [1, 4, 5, 1, 5, 8, 7, 5, 9, 6, 7, 4, 5, 6, 7, 0]
output: [0, 1, 1, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 8, 9]
```

## 10. 桶排序
桶排序，先准备好一个数据范围，先把相关的数据分在不同的“桶”中，再对桶中的小批量数据进行输出排序输出。
1. 准备好固定的数据范围，比如输入数据范围是：1-10000，我们可以准备100个桶，即第一个桶范围是1-100，第二个桶是101-200···
2. 遍历数据，把对应范围的数据放到桶中
3. 遍历桶，取出桶中的数据，然后进行排序输出

有此我们可以把桶排序的算法分为三部分：
- 生成桶：针对数据范围生成合适的桶这个操作是决定桶排序的时间复杂度的主要因素
- 把数据放进对应的桶中：数据放入桶中的操作算法有很多，比如：
	- 除了if/else if语句
	- switch/case语句
	- 向下取整求取浮点数范围的方法
	- 除以10、100、1000这样的大范围数划分范围
- 对于已经放进桶中的数据进行排序：因为此时桶中的数据内容已经相对来说比较小了，可以使用插入排序等排序方法，当然要是不嫌麻烦也可以使用快排等时间复杂度为O(nlogn)的方法

桶排序适用于：
- 数据内容不固定，可以是浮点的也可以是整型的，只需要动态计算桶的大小即可
- 数据的范围有限
```python
# -*- coding: utf-8 -*-
# author: www.lichangan.com

"""
桶排序
1）在额外空间充足的情况下，尽量增大桶的数量
2）使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
  个人理解，如果都是整数还可以用计数排序来计数统计然后排序，但是如果是一个连续空间内的排序，即统计的是一个浮点类型的数组成的数组，那么，就无法开辟一个对应的空间使其一一对应的存储。此时，我们需要新建一个带有存储范围的空间，来存储一定范围内的元素
空间复杂度：O(n)
时间复杂度: O(n)
稳定
"""


def bucket_sort(arr, max_num):
    """
    本算法是对浮点数进行排序，此处的放入桶中的方法为对浮点数取整
    """
    buf = {i: [] for i in range(int(max_num)+1)}  # 不能使用[[]]*(max+1)，这样新建的空间中各个[]是共享内存的
    arr_len = len(arr)
    for i in range(arr_len):
        num = arr[i]
        buf[int(num)].append(num)  # 将相应范围内的数据加入到[]中
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            arr.extend(sorted(buf[i]))  # 这里还需要对一个范围内的数据进行排序，然后再进行输出
    return arr


if __name__ == "__main__":
    lis = [3.1, 4.2, 3.3, 3.5, 2.2, 2.7, 2.9, 2.1, 1.55, 4.456, 6.12, 5.2, 5.33, 6.0, 2.12]
    print(bucket_sort(lis, max(lis)))
```
输出结果：
```linux
input: [3.1, 4.2, 3.3, 3.5, 2.2, 2.7, 2.9, 2.1, 1.55, 4.456, 6.12, 5.2, 5.33, 6.0, 2.12]
output: [1.55, 2.1, 2.12, 2.2, 2.7, 2.9, 3.1, 3.3, 3.5, 4.2, 4.456, 5.2, 5.33, 6.0, 6.12]
```

## 11. 基数排序
基数排序(LDS)，**只适用于整型排序，或者有固定小数点位数的浮点型数据排序**，其概念就是，根据不同位数的数字进行排序，最终得到排序结果。
1. 先从最小的位数开始进行排序，对于排序的结果存于对应的队列中
2. 遍历0-9的栈，把数据弹出成为新的数列
3. 对下一个位数的数据重复上述操作
4. 直到所有的位数的都被轮完，从队列里面取出的数据即有序数据
```python
def radix_sort(data):

    if not data:
        return []
    max_num = max(data)  # 获取当前数列中最大值
    max_digit = len(str(abs(max_num)))  # 获取最大的位数

    dev = 1  # 第几位数，个位数为1，十位数为10···
    mod = 10  # 求余数的除法
    for i in range(max_digit):
        radix_queue = [list() for k in range(mod * 2)]  # 考虑到负数，我们用两倍队列
        for j in range(len(data)):
            radix = int(((data[j] % mod) / dev) + mod)
            radix_queue[radix].append(data[j])

        pos = 0
        for queue in radix_queue:
            for val in queue:
                data[pos] = val
                pos += 1

        dev *= 10
        mod *= 10
    return data
```
结果：
```linux
input: [58, 14, 5, 16, 78, 2, 123, 158, 753, 32, 1, 9, 5]
output: [1, 2, 5, 5, 9, 14, 16, 32, 58, 78, 123, 158, 753]
```
