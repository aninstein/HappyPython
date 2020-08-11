package main

import "fmt"

func romanToInt(s string) int {
    romanMap := make(map[string]int)
    romanMap["I"] = 1
    romanMap["V"] = 5
    romanMap["X"] = 10
    romanMap["L"] = 50
    romanMap["C"] = 100
    romanMap["D"] = 500
    romanMap["M"] = 1000
    dataLen := len(s)
    j := 0
    for i:=0; i<dataLen; i++ {
        char := string(s[i])
        tmp := ""

    }
    fmt.Println(romanMap, dataLen)
    return 1
}

func main()  {
    romanToInt("111")
}