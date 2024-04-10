from random import randint
import random
#s = input('Enter symbols :')
q = str(randint(10000000,100000000))
print(q)
a = ''
ac = 0
d = {}

for now in q:
    if now not in d:
        d[now] = 0
    d[now] += 1
    if d[now] > ac:
        ac = d[now]
        a = now

print(a,'',ac)


