spis = list(map(int, input().split()))

def proizved(spis):
    sorted_spis = sorted(spis)

    if sorted_spis[0]*sorted_spis[1] > int(sorted_spis[-2]) * int(sorted_spis[-1]):
        a = sorted_spis[0]
        b = sorted_spis[1]
    else:
        a = sorted_spis[-2]
        b = sorted_spis[-1]
    print(a,'',b)
    return a,' ',b

proizved(spis)
