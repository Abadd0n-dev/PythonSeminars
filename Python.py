#task 1
def select(f,col):
    return[f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)]

data = '1 2 3 4 5 6 7 8 15 33 53 66'.split()

result = map(int,data)
result = where(lambda x: not x % 2,result)
result = list(map(lambda x:(x, x**2), result))
print(result)

#task 2
a = [x for x in range(100)]

res = list(filter(lambda x: not x % 2 , a))

print(res)