#task 1
listOfNums = [1, 12, 43, 1, 0, 22]
result = 0

for i in range(len(listOfNums) // 2):
    result += listOfNums[2 * i + 1]
for i in range(len(listOfNums)):

    if i % 2 != 0:
        result += listOfNums[i]
print(result)

#task 2
listOfNum = [2, 3, 4, 5, 6]
result = []
listOfNum =[2, 3, 5, 6]
for i in range(int(len(listOfNum)/2 + len(listOfNum)%2)):
    if len(listOfNum) % 2 == 0:
        if i >= len(listOfNum)//2:
            break
        else:
            result.append(listOfNum[i]*listOfNum[-(i + 1)])
    else:
        if i > len(listOfNum)//2:
            break
        else:
            result.append(listOfNum[i]*listOfNum[-(i + 1)])
print(result)

#task 3
listOfNums = [1.1, 1.2, 3.1, 5, 10.01]
listOfNumsAfterPoint = []

for num in listOfNums:
    if num % 1 != 0:
        listOfNumsAfterPoint.append(float('0.%s' % str(num).split('.')[1])) #listOfNumsAfterPoint.append(num % 1)
result = max(listOfNumsAfterPoint) - min(listOfNumsAfterPoint)
print(result)

#task 4
num = 45

def ToBynnary(number):
    result = ''    
    while(number != 0):    
            result = result + str(int(number % 2))
            number = int(number / 2)
    return result

print(ToBynnary(num))

#task 5
a = 8
def Fibonachi(num):
    fibonacchiRow = []
    firstNum = 0
    secondNum = 1
    result = 0
    i = 0
    while(i < num):
        if (i == 0):
            fibonacchiRow.append(0)
        if (i == 1):
            fibonacchiRow.append(1)
            fibonacchiRow.insert(0, -1)
        else:
            result = firstNum + secondNum
            firstNum = secondNum
            secondNum = result
            fibonacchiRow.append(result)
            if fibonacchiRow[0] > 0:
                fibonacchiRow.insert(0, -result)
            else: 
                fibonacchiRow.insert(0, result)
        i += 1
    return fibonacchiRow
print(Fibonachi(8))
