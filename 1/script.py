file = open('help.txt', 'r')
sum = ""
while True:
    line = file.readline()
    if not line:
        break
    allDigits= []
    for char in line:
        if char.isdigit():
            allDigits.append(char)
    if (len(allDigits) == 1):
        sum.append(allDigits[0])
    elif(len(allDigits) == 0):
        sum = sum
    elif (len(allDigits) == 2):
        sum += int(allDigits[0] + allDigits[1])
    elif (len(allDigits) > 2):
        secondToLastIndex = len(allDigits) - 1
        del allDigits[1:secondToLastIndex]
        sum += int(allDigits[0] + allDigits[1])
    print(sum)
