package main

import "fmt"

func main() {
    data := []int{1, 5, 7, 1, 8, 9, 4, 2, 3}
    fmt.Println(insertSort(data))
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
                    data[j] = data[j-1]
                }else{
                    data[j] = tmp
                    break
                }
            }
        }
    }
    return data
}

