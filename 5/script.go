package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		// fmt.Println("Error opening file:", err)
		return
	}
	var input string  = string(file)

	for _, line := range strings.Split(input, ":") {
		if(line == "") {
			continue
		}
		fmt.Println("Line:", line)
		
		seeds := line[1]
		// seedSoil := line[3]
		// soilFert := line[5]
		// fertWater := line[7]
		// waterSun := line[9]
		// sunTemp := line[11]
		// tempHumid := line[13]
		// humidLoc := line[15]

		fmt.Println("seeds:", seeds)
		// fmt.Println("seedSoil:", seedSoil)
		// fmt.Println("soilFert:", soilFert)
		// fmt.Println("fertWater:", fertWater)
		// fmt.Println("waterSun:", waterSun)
		// fmt.Println("sunTemp:", sunTemp)
		// fmt.Println("tempHumid:", tempHumid)
		// fmt.Println("humidLoc:", humidLoc)
	}
}
	
