xyz = set(map(str,input().split()))
N = str(input())

def OpenCalculator(N,xyz):
    N_set = set(list(N))
    otvet = len(N_set) - len(N_set & xyz)
    return otvet

print(OpenCalculator(N,xyz))