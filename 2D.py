spis = list(map(int, input().split()))
def sosed(spis):
    counter = 0
    for i in range(1,len(spis)-1):
        if spis[i] > spis[i-1] and spis[i] > spis[i+1]:
            counter += 1
    return counter
print(sosed(spis))