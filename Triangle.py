def nomer():
    m = input()
    a = input()
    b = input()
    c = input()
    string = [m,a,b,c]
    repl = {'+7':'8','-':'','(':'',')':''}
    nstring = []
    cod = '8495'
    for i in string:
        for old, new in repl.items():
            i = i.replace(old, new)
        nstring.append(int(i))

    k = 0
    for i in nstring:
        if len(str(i)) < 11:
            nstring[k] = int(cod + str(i))
        k += 1

    for j in range(1,len(nstring)):
        if nstring[0] == nstring[j]:
            print('YES')
        else:
            print('NO')

nomer()






















"""
r i in nstring:
    if len(nstring[i]) < 11 :
        string[i] = string[i:1] + cod + string[1:i]
"""



"""
for i in string:
    nstr = ''
    for j in i:
        if j in repl:
            nstr += repl[j]
        else:
            nstr += j
    nstring.append(nstr)


print(nstring)
"""
