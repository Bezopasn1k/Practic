
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
def peresech(list1,list2):
    list3 = sorted(set(list1) & set(list2))
    return list3

print(" ".join(map(str, peresech(list1,list2))))