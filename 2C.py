'''''''''
from random import randint
N = randint(1, 1000)
mv = -1000
mxv = 1000

array = [randint(mv, mxv) for _ in range(N)]
print('Массив:',array)
x = randint(-1000, 1000)
print('ИКС:',x)
'''''''''
N = int(input())
array = list(map(int, input().split()))
x = int(input())

def bl(N,x,array):
    count = 2001
    t = 0

    for i in range(0,N):
        if (abs(x - array[i]) < count):
            count = abs(x - array[i])
            t = array[i]

    return t

print(bl(N,x,array))