#구글링
import sys

input = sys.stdin.readline

n = int(input())

ans = 0
row = [0] * n
#2차원 배열을 하나로 압축, 인덱스 = 행, 배열 값 = 열
#퀸 설치 조건 : 같은 행, 열 그리고 대각선에 다른 퀸이 있으면 안 됨

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): #열이 같은지, 대각선이 같은지 비교
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n: #끝까지 돌았으면
        ans += 1 #가능한 경우의 수인걸로 판단
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x): #False 나오면 그 자리에는 퀸 설치 못 하는 것
                n_queens(x+1)

n_queens(0) #첫번째 행부터 시작
print(ans)