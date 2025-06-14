T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apt = [[0] * n for _ in range(k + 1)]

    apt[0] = [i for i in range(1, n + 1)]

    for i in range(1, k + 1):
        apt[i][0] = apt[i - 1][0] #맨 처음 호수는 바로 밑 층만

        for j in range(1, n): #바로 밑 층 + 이전 호수
            apt[i][j] += apt[i - 1][j]
            apt[i][j] += apt[i][j - 1]
    
    print(apt[k][n - 1])