package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	data, err := os.ReadFile("2015/day_1/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	inputData := string(data)

	idx := 0
	currentFloor := 0
	firstEntry := true
	var basementIdx int
	for idx < len(inputData)-1 {
		if currentFloor == -1 && firstEntry {
			basementIdx = idx
			firstEntry = false
		}
		if string(inputData[idx]) == "(" {
			currentFloor += 1
		} else {
			currentFloor -= 1
		}
		idx += 1
	}

	fmt.Println(currentFloor, basementIdx)
}
