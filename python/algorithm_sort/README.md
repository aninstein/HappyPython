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
## 10. 基数排序
## 11. 桶排序