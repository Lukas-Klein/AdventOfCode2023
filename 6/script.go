package main

import "fmt"

func main() {
	time := []int{42, 68, 69, 85}
	distance := []int{284, 1005, 1122, 1341}

	fmt.Println("part1", part1(time, distance))

	time2 := 42686985
	distance2 := 284100511221341

	fmt.Println("part2", part2(time2, distance2))

}

func part1(time []int, distance []int) int {
	recordsBreaksValue := 1

	for index, t := range time {
		recordBreaks := 0
		for d := 0; d < t; d++ {
			travelledDistance := (t - d) * d
			if travelledDistance > distance[index] {
				recordBreaks++
			}
		}
		recordsBreaksValue = recordsBreaksValue * recordBreaks
	}
	return recordsBreaksValue
}

func part2(time int, distance int) int {
	recordBreaks := 0
	for d := 0; d < time; d++ {
		travelledDistance := (time - d) * d
		if travelledDistance > distance {
			recordBreaks++
		}
	}
	return recordBreaks
}
