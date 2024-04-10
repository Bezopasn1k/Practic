def poisk(ryad):
    spis = [0] * (len(ryad)+1)
    count =0
    for i in range(1,len(spis)):
        spis[i] = spis[i-1] + ryad[i-1]
    for i in range(l,r):

        return count


l = 0
r = 1
N,K = list(map(int, input().split()))
ryad = list(map(int, input().split()))
print(ryad)
print(N,K)
print(poisk(ryad))