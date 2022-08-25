#task 1
firstValue = int(input('enter the first number = '))
secondValue = int(input('enter the second number = '))

if firstValue ** firstValue == secondValue:
    print(f'{secondValue} is a square {firstValue}')
if secondValue ** secondValue == firstValue:
    print(f'{firstValue} is a square {secondValue}')
else:
    print('numbers are not squares')

#task 2
list = [234,43,432,65,111]
print(max(list))

#task 3
n = int(input('enter the first number = '))
secondValue = range(-n,n)
for i in secondValue:
    print(f'print all numbers from -n to n {i}')

#task 4
fractionalNumber = 1233325.434243142
string = str(fractionalNumber)

print(string[0])

#task 5
firstValue = 30
if (firstValue%5 == 0 and firstValue%10 == 0) or (firstValue%15 == 0 and not firstValue % 30 == 0):
    print ("all right")

#task 6
firstValue = int(input('enter a number from 0 to 6: '))
my_dict = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
if firstValue == 5 and firstValue == 6:
    print(f"{my_dict.get(firstValue)} day off")
else:
    print(f"{my_dict.get(firstValue)} not a day off")

#task 7
x = [True, False]
y = [True, False]
z = [True, False]
count = 0
for i in x:
    for j in y:
        for g in z:
            count += 1
            print(f"{count} {not (x or y  or z) == (not x and not y and not z)}")

#task 8
x = int(input('enter x'))
y = int(input('enter y'))

if (x>0) and (y>0):
    print('1 quarter')
elif (x>0) and (y<0):
    print('2 quarter')
elif (x<0) and (y<0): 
    print('3 quarter')
elif (x<0) and (y>0):
    print('4 quarter')
else:
    print('point lies on the axis')

#task 9
print("enter number quarter")
numOfQuadro = int(input())

def whichCoords(numOfQuadro):
        if numOfQuadro == 1:
            return "1 to infinity, y = 1 to infinity"
        if numOfQuadro == 2:
            return "1 to infinity, t = 1 to -infinity"
        if numOfQuadro == 3:
            return "-1 to -infinity, t = -1 to -infinity"
        if numOfQuadro == 3:
            return "-1 to -infinity, t = 1 to infinity"
print(whichCoords(numOfQuadro))

#task 10
import math

print('Enter the coordinates of the first point')
print('x1 =')
x1 = int(input())
print('y1 =')
y1 = int(input())
print('z1 =')
z1 = int(input())
print('x2 =')
print('Enter the coordinates of the second point')
x2 = int(input())
print('y2 =')
y2 = int(input())
print('z2 =')
z2 = int(input())
point1 = (x1, y1, z1)
point2 = (x2, y2, z2)

def DistanceBetweenPoint(point1, point2):

    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))     

print(DistanceBetweenPoint(point1, point2))

#task 11
number = int(input("Enter number: "))
for i in range(number):
    result = (-3)**i
    print(result)

#task 12
N = int(input())
dict = {}
for i in range(1, N + 1):
    res = 3 * i + 1        
    dict.update({i:res})
print(dict)

#task 13
string1 = str(input('Enter the first line: '))
string2 = str(input('Enter the second line: '))

print(f'The second line is included in the first {string1.count(string2)} times/times')

#task 14
num = input('Enter a number with a dot')
result = 0
for i in range(len(num)):
    if (num[i] == '.'):
        continue
    result += int(num[i])
print(result)

#task 15
num = int(input())
arr = []
for i in range(0, num + 1): 
    if (i == 0):
        arr.append(1)
    else:
        arr.append(arr[i - 1] * (i + 1))
print(arr)

#task 16
number = int(input())
listNum = []
result = 0
for i in range(1, number + 1):
    listNum.append((1 + 1 / i) ** i)
for j in range(int(len(listNum))):
    result += listNum[j]
print(result)

#task 17

#task 18
import random
result = list(range(1, 9))
random.shuffle(result)
print(result)

#task 19
from time import perf_counter

len_of_num = input('Enter the len of number: ')
output_number = 0
if len_of_num.isdigit():
    current_time = int(str(perf_counter()).split('.', 1)[-1])
    output_number = (str(current_time ** (int(len_of_num) // 6 + 1)))[:int(len_of_num)]
    print(output_number)
else:
    print('Please check if the entered value is a number')