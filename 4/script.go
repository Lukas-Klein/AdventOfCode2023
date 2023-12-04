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

func part2(myNumbers []string, winningNumbers []string) int {
	points := 0
	for _, number := range myNumbers {
		if number != "" {
			if slices.Contains(winningNumbers, number) {
				points++
			}
		}
	}
	return points
}

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	fmt.Println("File opened successfully")
	input := string(file)
	fmt.Println(string(file))

	for _, line := range strings.Split(input, "\n") {
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
		fmt.Println("Winner:", winnerNumbers)
		fmt.Println("Mine:", myNumbers)

		points := part2(myNumbers, winnerNumbers)
		for i := 1; i < points; i++ {
			// input = input +
		}
	}

}
