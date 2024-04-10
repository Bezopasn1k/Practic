def pomosh():
    k1 = int(input())
    m = int(input())
    k2 = int(input())
    p2 = int(input())
    n2 = int(input())

    spis = [k1,m,k2,p2,n2]

    for i in range(0,len(spis)):
        if spis[i] <= 0 or spis[i] > 10**6:
            print(-1,-1)
            return 0

    a = ((k2-1)/(m*(p2-1)+n2))
    b = ((k2-1)/(m*(p2-1)+n2-1))
    print(a,b)

pomosh()

