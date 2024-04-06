import sys

def reverse(arr, X, Y):
    for y in range(Y, Y+3):
        for x in range(X, X+3):
            if (x >= M) or (y >= N):
                return -1
            
            arr[y][x] += 1
            arr[y][x] %= 2

    return 1
    
N, M = map(int, input().split())


a = [list(map(int,list(input().rstrip()))) for _ in range(N)]
b = [list(map(int,list(input().rstrip()))) for _ in range(N)]

flag = 1
cnt = 0
for y in range(N):
    for x in range(M):

        if a[y][x] != b[y][x]:
            flag = reverse(a, x, y)

            if flag == -1:
                print(-1)
                exit()
            cnt += 1

print(cnt)