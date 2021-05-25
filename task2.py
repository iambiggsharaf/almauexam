a = [3, 6, 12, 55]

maxDivisor = max(a)

myDict = {}

for i in range(1, maxDivisor + 1):
    myDict[i] = 0

for i in a:
    for j in range(1, i + 1):
        if i % j == 0:
            myDict[j] += 1

print(myDict)