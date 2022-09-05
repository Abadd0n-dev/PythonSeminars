#task1
str1 = list(input().split())
str1 = ['abc', 'hfghdfg', 'sfsefs', 'fgjnggghfh']
str2 = [str1[x] for x in range(len(str1)) if not str1[x].__contains__("abc")]
strResult = ''
for i in str2:
    strResult += i + ' '
print(strResult.strip())

#task2
numsOfCandies = 2021
counter = 0
def playerTurn(numsOfCandies):
    if numsOfCandies == 0:
        return -1
    takenCandies = int(input("Enter how many sweets you are taking: "))
    while takenCandies <= 0 or takenCandies > 28:
        takenCandies = int(input('You can only take from 1 to 28 sweets. Try again: '))
        if numsOfCandies < takenCandies:
             print(f'left {numsOfCandies} sweets, enter a number from 1 to {numsOfCandies}')
    if numsOfCandies < takenCandies:
        while takenCandies <= 0 or takenCandies > numsOfCandies:    
            takenCandies = int(input(f'left {numsOfCandies} sweets, enter a number from 1 to {numsOfCandies}: '))    
    numsOfCandies -= takenCandies   
    return numsOfCandies

while numsOfCandies > 0:
        if numsOfCandies > 0:
            print('Player 1 turn')
            numsOfCandies = playerTurn(numsOfCandies)
            counter += 1
        if numsOfCandies > 0:
            print('Player 2 turn')
            numsOfCandies = playerTurn(numsOfCandies)
            counter += 1
if counter % 2 == 0:
    print('Player 2 won')
else:
    print('Player 1 won')

#With a bot
from random import randint as randint
numsOfCandies = 200
counter = 0
def playerTurn(numsOfCandies):
    if numsOfCandies == 0:
        return -1
    takenCandies = int(input("Player 1 won "))
    while takenCandies <= 0 or takenCandies > 28:
        takenCandies = int(input('You can only take from 1 to 28 sweets. Try again: '))
        if numsOfCandies < takenCandies:
             print(f'left {numsOfCandies} sweets, enter a number from 1 to {numsOfCandies}')
    if numsOfCandies < takenCandies:
        while takenCandies <= 0 or takenCandies > numsOfCandies:    
            takenCandies = int(input(f'left {numsOfCandies} sweets, enter a number from 1 to {numsOfCandies}: '))    
    numsOfCandies -= takenCandies   
    return numsOfCandies

def pcTurn(numsOfCandies):
    takenCandies = randint(1, 28)
    while takenCandies > numsOfCandies:
        takenCandies = randint(1, 28)
    if numsOfCandies <= 28:
        takenCandies = numsOfCandies
    if 28 < numsOfCandies < 56:
        takenCandies = numsOfCandies - 29
        print(f'Computer picks up {takenCandies} candy. ', end='')
    numsOfCandies -= takenCandies
    print(f'Computer picks up {takenCandies} candy. Candy left: {numsOfCandies}')
    return numsOfCandies

#task 3
game_matrix = [[None, None, None], [None, None, None], [None, None, None]]
game_is_on = True
while game_is_on:
    move = input()
    exec("game_matrix" + move)
    for row in game_matrix:
        print(row)
    
    reference_matrix = [
        game_matrix[0],
        game_matrix[1],
        game_matrix[2],
        [i[0] for i in game_matrix],
        [i[1] for i in game_matrix],
        [i[2] for i in game_matrix],
        [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
        [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] != None:
            print("Game over!")
            game_is_on = False
            break