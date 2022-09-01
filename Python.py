#task 1
num = int(input())
listOfSimpleMultiplier = []
i = 2
while num > 1:
    while num % i == 0:
        listOfSimpleMultiplier.append(i)
        num //= i
    i += 1
print(listOfSimpleMultiplier)

#task 2
listOfNums = [1, 2, 3, 5, 1, 5, 3, 10]
listOfUnicNums = []
for i in listOfNums:
    if i not in listOfUnicNums:
        listOfUnicNums.append(i)
print(listOfUnicNums)

#task 3
k = int(input('Enter the maximum exponent for the polynomial: '))
resultString = ''
if k >= 0:
    while k > 0:
        if k == 1:
            resultString += f'{randint(0, 100)}*x + '
        else:
            resultString += f'{randint(0, 100)}*x^{k} + '
        k -= 1

else:
    while k < 0:
        resultString += f'{randint(0, 100)}*x^{k} + '
        k += 1
resultString += f'{randint(0, 100)} = 0'
with open(r'hw4.txt','+a') as f:
    f.write(resultString + '\n')
print(resultString)