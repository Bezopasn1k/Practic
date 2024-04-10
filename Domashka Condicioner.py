def Cond(tr,tc,v):

    if (v == 'heat' and tr < tc) or (v == 'freeze' and tr > tc) or (v == 'auto' and tr != tc):
        return tc
    else:
        return tr
tr,tc = list(map(int, input().split()))
v = input()
print(Cond(tr,tc,v))