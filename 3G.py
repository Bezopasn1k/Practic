N = int(input())
def Cherepah(N):
    ab = set()
    counter = 0
    for i in range(N):
        a, b = list(map(int, input().split()))
        x = a,b
        if a + b != N - 1:
            counter +=1
            ab.add(x)
        else:
            if x not in ab:
                ab.add(x)
            else:
                counter += 1
    N = N - counter
    return N

print(Cherepah(N))