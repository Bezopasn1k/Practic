N,K,M = list(map(int, input().split()))
def detal(N,K,M):

    a = N % K
    k = (N // K) * (K // M)
    b = (K - (K // M) * M) * (N // K)
    ab = a + b

    if K > N or M > K:
        return 0

    while ab >= K:
        N = ab
        a = N % K
        b = (K - (K // M) * M) * (N // K)
        ab = a + b
        k = k + (N // K) * (K // M)
    return k

detal(N,K,M)

print(detal(N,K,M))


