myArray = [1, 34, 1, 2, 4, 5, 7, 8, 0, 1, 2, 4]
counterDict = {}

for i in myArray:
    if i not in counterDict:
        counterDict[i] = 0
    counterDict[i] += 1

sortedOut = sorted(counterDict.items(), key=lambda x: x[1])

print(k for k, v in sortedOut[-2:])
