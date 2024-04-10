
def hoh():

    s = input("Введите последовательность :  ")
    ans = ''
    anscnt = 0
    det = {}
    for now in s:
        if now not in det:
            det[now] = 0
        det[now] += 1

        if det[now] > anscnt:
            anscnt = det[now]
            ans = now

    print(ans,anscnt)


if __name__ == '__main__':
    hoh()
