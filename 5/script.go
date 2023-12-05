package main

import (
	"fmt"
	"os"
)

func main(){
	file, err := os.ReadFile("input.txt")
	if err != nil {
		// fmt.Println("Error opening file:", err)
		return
	}
	fmt.Println(file)
}