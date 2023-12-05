package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

func getPoints(myNumbers []string, winningNumbers []string) int {
	points := 0
	for _, number := range myNumbers {
		if number != "" {
			if slices.Contains(winningNumbers, number) {
				if points == 0 {
					points = 1
				} else {
					points = points * 2
				}
			}
		}
	}
	return points
}

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		// fmt.Println("Error opening file:", err)
		return
	}
	input := string(file)

	for _, line := range strings.Split(input, "\n") {
		// // fmt.Println("Line:", line)
		// Split the line using ": " as a delimiter
		parts := strings.Split(line, ": ")
		if len(parts) != 2 {
			// Skip lines that don't follow the expected format
			continue
		}

		allNumbers := parts[1]
		// Split the numbers using " | " as a delimiter
		numbers := strings.Split(allNumbers, " | ")
		if len(numbers) != 2 {
			// Skip lines that don't follow the expected format
			continue
		}

		winnerNumbers := strings.Split(numbers[0], " ")
		myNumbers := strings.Split(numbers[1], " ")

		points := getPoints(myNumbers, winnerNumbers)
		fmt.Println(points)

	}
}
