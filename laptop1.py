def laptop(y):

    a = int(y[0])
    b = int(y[1])
    c = int(y[2])
    d = int(y[3])
    n = 0
    n1 = 1001
    max1 = 0
    max2 = 0
    min1 = 0
    min2 = 0

    spis =[[a,b],[c,d]]

    if a >= b:
        max1 = a
        min1 = b
    else:
        max1 = b
        min1 = a

    if c >= d:
        max2 = c
        min2 = d
    else:
        max2 = c
        min2 = d



    if a >= b:
        max1 = a
        min1 = b
    else:
        max1 = b
        min1 = a

    if c >= d:
        max2 = c
        min2 = d
    else:
        max2 = c
        min2 = d



    if min1 >= max2 :
        x = max1 + min2
        y = min1
        return x, y

    if min2 >= max1 :
        x = max2 + min1
        y = min2
        return x, y

    if max1 >= max2 and max2 >= min1 :
        x = max1
        y = min1 + min2
        return x, y
    if max2 >= max1 and max1 >= min2 :
        x = max2
        y = min2 + min1
        return x, y
    



x = input()
y = x.split()
result = laptop(y)
x, y = result
print(x, y)