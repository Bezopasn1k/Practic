def peresech(list1,list2):
    list3 = sorted(set(list1) & set(list2))
    return list3
N, M =list(map(int, input().split()))
KubA = set()
KubB = set()
for _ in range(N):
   KubA.add((int(input())))

for _ in range(M):
   KubB.add((int(input())))

sort1 = peresech(KubA,KubB)
for a in sort1:
    KubA.remove(a)
    KubB.remove(a)

Anyaost = sorted(KubA)
Bobost =  sorted(KubB)

print(len(sort1))
print(" ".join(map(str, sort1)))
print(len(Anyaost))
print(" ".join(map(str, Anyaost)))
print(len(Bobost))
print(" ".join(map(str, Bobost)))



