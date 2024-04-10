
N = int(input())
spis = list(map(int, input().split()))
newlist = spis
def proverka(N,spis):
    if N % 2 == 0 and spis[0:int((N / 2))] == list(reversed(spis[int(N / 2):])):
        return True
    elif N % 2 != 0 and spis[0:int((N // 2))] == list(reversed(spis[int((N // 2) + 1):])):
        return True
    return False

def simmetr(N,newlist):
    if proverka(N,newlist) == True:
        print(0)
        return 0
    m = N
    rlist = list(reversed(newlist))
    newlist.extend(rlist[-1:])
    i = -1
    while proverka(N,newlist) == False:
        del newlist[i:]
        i += -1
        newlist.extend(rlist[i:])
        N = len(newlist)

    m = N - m
    lastlist = list(newlist[-m:])
    print(m)
    print(*lastlist, sep = ' ')
    return m,lastlist

simmetr(N,newlist)

