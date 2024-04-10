A = str(input())
B = str(input())
def genom(A,B):
    Bset = set()
    counter = 0
    for j in range(len(B)-1):
        Bset.add(B[j] + B[j+1])
    for i in range(len(A)-1):
        if A[i] + A[i+1] in Bset:
            counter += 1
    return counter
print(genom(A,B))