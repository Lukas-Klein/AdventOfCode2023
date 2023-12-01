# file = open('help.txt', 'r')
# sum = str("")
# globalSum = 0
# spelledDigits= ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# test = "two1nine"

# def checkForDigit(line, allDigits):
#     for i, digit in enumerate(spelledDigits):
#         if digit in line:
#             print(line)
#             print(digit)
#             print(str(spelledDigits.index(digit) + 1))
#             allDigits.append(str(spelledDigits.index(digit) + 1))

# while True:
#     line = file.readline()
#     if not line:
#         break
#     allDigits= []
#     checkForDigit(line, allDigits)
#     for char in line:
#         if char.isdigit():
#             allDigits.append(char)
#     # print(allDigits)
#     if(len(allDigits) == 0): 
#         sum = sum
#     else:
#         if(len(allDigits) == 1):
#             sum = allDigits[0] + allDigits[0]
#             globalSum += int(sum)
#         elif (len(allDigits) == 2):
#             sum = allDigits[0] + allDigits[1]
#             globalSum += int(sum)
#         else:
#             del allDigits[1: len(allDigits)-1]
#             sum = allDigits[0] + allDigits[1]
#             globalSum += int(sum)
# print(globalSum)
file = open('help.txt', 'r')
globalSum = 0
spelledDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def checkForDigit(line, allDigits):
    for digit in spelledDigits:
        if digit in line:
            allDigits.append(str(spelledDigits.index(digit) + 1))
            break

while True:
    line = file.readline()
    if not line:
        break
    allDigits = []
    checkForDigit(line, allDigits)
    
    # Add the first and last regular digits
    for char in line:
        if char.isdigit():
            allDigits.append(char)
    if len(allDigits) >= 2:
        first_digit = allDigits[0]
        last_digit = allDigits[-1]
        allDigits = [first_digit, last_digit]

    if allDigits:
        sum_str = ''.join(allDigits)
        globalSum += int(sum_str)

print(globalSum)


        
    
