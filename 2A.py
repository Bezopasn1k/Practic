spis = list(map(int, input().split()))
def vozr(spis):
    for i in range(1,len(spis)):
        if spis[i] <= spis[i-1]:
            return 'NO'
    return 'YES'


print(vozr(spis))