def func():
    a = float(input())
    b = float(input())
    c = float(input())

    if a != int(a) or b != int(b) or c != int(c):
        print('NO SOLUTION')
        return 0
    else:
        a = int(a)
        b = int(b)
        c = int(c)

    if c >= 0:
        if a != 0 and ((c ** 2 -b)/a) == int((c ** 2 -b)/a):
            print(int((c ** 2 -b)/a))
        elif a == 0 and b == c**2 :
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
         print('NO SOLUTION')

func()

