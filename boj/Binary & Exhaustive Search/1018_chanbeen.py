import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]

result = []

for i in range(N + 1 - 8):
    for j in range(M + 1 - 8):
        paint1 = 0
        paint2 = 0
        #paint1 : 첫 칸이 검은색, paint2 : 첫 칸이 흰색
        for p in range(i, i+8):
            for q in range(j, j+8):
                if (p + q) % 2 == 0: #체스판에는 인덱스의 특징이 존재
                    if board[p][q] != 'B':
                        paint1 += 1
                    elif board[p][q] != 'W':
                        paint2 += 1
                else:
                    if board[p][q] != 'W':
                        paint1 += 1
                    elif board[p][q] != 'B':
                        paint2 += 1
        
        result.append(min(paint1, paint2))

print(min(result)) #최솟값