package main

import "fmt"

func main() {
    data := []int{1, 5, 7, 1, 8, 9, 4, 2, 3, -1, 14, 41, -22}
    fastSort2(data, 0, len(data)-1)
    fmt.Println(data)
}


func bubbleSort(data []int) []int{
    if data == nil || len(data) == 0 {
        return []int{}
    }
    dataLen := len(data)
    for i := 0; i < dataLen; i++{
        for j := i + 1; j < dataLen; j++{
            if data[i] > data[j] {
                data[i], data[j] = data[j], data[i]
            }
        }
    }
    return data
}


func selectSort(data []int) []int{
    if data == nil || len(data) == 0{
        return []int{}
    }

    dataLen := len(data)
    for i := 0; i < dataLen; i++ {
        tmp := i
        for j := i+1; j < dataLen; j++ {
            if data[tmp] < data[j] {
                tmp = j
            }
        }
        if tmp != i {
            data[i], data[tmp] = data[tmp], data[i]
        }
    }
    return data
}


func insertSort(data []int) []int {
    if data == nil || len(data) == 0 {
        return []int{}
    }

    dataLen := len(data)
    for i := 1; i < dataLen; i++ {
        if data[i-1] > data[i] {
            tmp := data[i]
            for j := i; j > 0; j-- {
                if tmp < data[j-1]{
                    data[j] = data[j-1]  //挪动字段
                } else {
                    data[j] = tmp
                    break
                }
            }
        }
    }
    return data
}


// 希尔排序，插入排序改进版本
//    1. 把队列按照步长，分序列先做直接插入
//    2. 缩小等分步长做直接插入
//    3. 等分步长为1时候停止
func shellSort(data []int) []int {
    if data == nil || len(data) == 0 {
        return []int{}
    }

    dataLen := len(data)
    step := int((dataLen - 1) / 2)
    for step >= 1{
        step = int(step)
        for i := step; i < dataLen; i++ {
            tmp := data[i]
            j := i - step
            for j >= 0 && data[j] > tmp{  // 就是插入排序的挪动元素的步骤
                data[j+step] = data[j]
                j -= step
            }
            data[j+step] = tmp  // 完成元素的交换
        }
        step /= 2
    }
    return data
}

// 快速排序1
// 这种方法虽然便于理解，但是耗费空间比较多
func fastSort1(data []int) []int {
    if data == nil || len(data) == 0 {
        return []int{}
    }

    dataLen := len(data)
    var left, mid, right []int
    index := data[0]
    for i := 0; i < dataLen; i++ {
        if data[i] > index{
            right = append(right, data[i])
        }else if data[i] < index {
            left = append(left, data[i])
        }else {
            mid = append(mid, data[i])
        }
    }
    leftList := append(fastSort1(left), mid...)
    return append(leftList, fastSort1(right)...)
}


// 快速排序2
// 类似java和c那种，数组长度不能改变，没有类似python的list或者go的切片那样的数据类型
// 这种情况下就是充分的使用数组之间数据交换的方式进行数据排序
// 这种方法主要是不断的寻找最佳标定位置的方法
func fastSort2(data []int, left, right int) {
    if left < right{
        pos := pattion(data, left, right)
        fastSort2(data, left,  pos-1)
        fastSort2(data, pos+1,  right)
    }
}

func pattion(data []int, left, right int) int {
    index := data[right]  // 选用最后一个值作为标志
    i := left - 1
    for j := left; j < right; j++ {
        if index > data[j] {
            i ++
            swap(data, i, j)
        }
    }
    swap(data, i+1, right)
    return i+1
}

func swap(data []int, i, j int) {
    data[i], data[j] = data[j], data[i]
}