package main

import "fmt"

func main() {
    data := []int{1, 5, 7, 1, 8, 9, 4, 2, 3}
    fmt.Println(bubbleSort(data))
}


func bubbleSort(data []int) []int{
    if data == nil || len(data) == 0 {
        return nil
    }

    dataLen := len(data)
    for i := 0; i < dataLen; i++{
        for j := i + 1; j < dataLen; j++{
            if data[i] > data[j] {
                tmp := data[i]
                data[i] = data[j]
                data[j] = tmp
            }
        }
    }
    return data
}
