def ass(spis):
    p = spis[0]
    for i in range(1,len(spis)):
        if spis[i] <= p:
            return False
        p = spis[i]
    return True

def wa(spis):
    p = spis[0]
    for i in range(1,len(spis)):
        if spis[i] < p:
            return False
        p = spis[i]
    return True

def des(spis):
    p = spis[0]
    for i in range(1,len(spis)):
        if spis[i] >= p:
            return False
        p = spis[i]
    return True

def wd(spis):
    p = spis[0]
    for i in range(1,len(spis)):
        if spis[i] > p:
            return False
        p = spis[i]
    return True

def cons(spis):
    if len(set(spis)) == 1:
        return True
    return False

def fo(spis):
    if cons(spis) == True:
        return 'CONSTANT'
    elif ass(spis) == True:
        return 'ASCENDING'
    elif wa(spis) == True:
        return 'WEAKLY ASCENDING'
    elif des(spis) == True:
        return 'DESCENDING'
    elif wd(spis) == True:
        return 'WEAKLY DESCENDING'
    else:
        return 'RANDOM '


spis = []
while True:
    num = float(input())
    if num == -2000000000:
        break
    spis.append(num)


print(fo(spis))






