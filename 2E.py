n = int(input())
spis = list(map(int, input().split()))
def lepesh(n,spis):
    '''''
    mylist = sorted(set(spis))
    piz = {}
    for i in range(0,len(mylist)):
        piz[mylist[i]] = len(mylist)-i
    '''''
    max_index = spis.index(max(spis))
    k = 10000
    counter = 1
    for i in range(max_index + 1,n - 1):
        if spis[i] % 5 == 0 and spis[i] % 10 != 0 and spis[i+1] < spis[i]:
            k = spis[i]
        return 0
    for j in range(0,len(spis)):
        if spis[j] > k:
            counter += 1
    return counter




print(lepesh(n,spis))