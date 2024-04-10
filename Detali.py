def kol(spis):
    d = {}
    n = 0
    for i in spis:
        if i not in d:
            d[i] = i
            n += 1
    return n

spis = list(map(int, input().split()))
print(kol(spis))