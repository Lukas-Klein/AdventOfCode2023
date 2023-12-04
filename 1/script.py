# file = open('input.txt', 'r')
# globalSum = 0
# spelledDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# def replaceDigitWithInt(line):
#     for i, digit in enumerate(spelledDigits, start=1):
#         line = line.replace(digit, str(i))
#     return line

# while True:
#     line = file.readline()
#     if not line:
#         break
#     allDigits = []
#     newLine = replaceDigitWithInt(line)
    
#     # Add the first and last regular digits
#    # Extract the first and last regular digits
#     allDigits = [char for char in newLine if char.isdigit()]
#     if len(allDigits) >= 2:
#         first_digit = allDigits[0]
#         last_digit = allDigits[-1]
#         allDigits = [first_digit, last_digit]

#     if first_digit is not None and last_digit is not None:
#         sum_str = first_digit + last_digit
#         globalSum += int(sum_str)

# print(globalSum)


import re

file = open('input.txt')
lines = file.readlines()

ouput_number = 0
digits_to_int = {
	"one": 1, "1": 1,
	"two": 2, "2": 2,
	"three": 3, "3": 3,
	"four": 4, "4": 4,
	"five": 5, "5": 5,
	"six": 6, "6": 6,
	"seven": 7, "7": 7,
	"eight": 8, "8": 8,
	"nine": 9, "9": 9
}

for line in lines:
	digits = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))", line)
	parsed_digits = [digits_to_int[num] for num in digits]
	number = str(parsed_digits[0]) + str(parsed_digits[-1])
	#print(line, parsed_digits, number)
	ouput_number = ouput_number + int(number)

print(ouput_number)    
    
