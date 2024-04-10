N, M, K = list(map(int, input().split()))

def pole(M,N,K):
    if K != 0:
        pq = []
        for i in range(0,K):
            p, q = list(map(int, input().split()))
            wor = []
            for j in range(0,1):
                wor.append(p)
                wor.append(q)
            pq.append(wor)

    matrix = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        matrix.append(row)

    k = 0
    for i in range(0,K):
        k += 1
        n = pq[i][0] - 1
        m = pq[i][1] - 1
        matrix[n][m] = '*'

        for x in range(max(0, n - 1), min(N, n + 2)):
            for y in range(max(0, m - 1), min(M, m + 2)):
                if matrix[x][y] != '*':
                    matrix[x][y] += 1

    for row in matrix:
        print(' '.join(map(str, row)))

    return matrix


pole(M,N,K)


'''''''''
matrix[n][m-1] = k
matrix[n][m+1] = k
matrix[n+1][m] = k
matrix[n+1][m+1] = k
matrix[n+1][m-1] = k
matrix[n-1][m] = k
matrix[n-1][m+1] = k
matrix[n-1][m-1] = k
'''''''''

'''     
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '*':
                matrix[i][j-1] += 1
                matrix[i][j+1] += 1
                matrix[i+1][j] += 1
                matrix[i+1][j+1] += 1
                matrix[i+1][j-1] += 1
                matrix[i-1][j] += 1
                matrix[i-1][j+1] += 1
                matrix[i-1][j-1] += 1
'''