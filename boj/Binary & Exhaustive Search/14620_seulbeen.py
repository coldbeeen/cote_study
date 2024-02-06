#재귀함수?
#가로방향으로 진행하면서 재귀 호출하면서 세로방향으로 내려간다? 검사는 어케하지?
import sys
# 본래 자리를 포함한 4방향에 이미 꽃을 심었다면
# False를 아니면 True를 리턴
def check(a, b):
    for i in range(5):
        x = a + di[i]
        y = b + dj[i]
        if visited[x][y] == 1:
            return False
    return True
 
 
def recur(cur):
    global total, answer
    
    # 꽃을 3개 다 심었을 때 최소 코스트 갱신
    if cur == 3:
        answer = min(answer, total)
        return
 
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            # 5 공간에 이미 심지 않았다면
            if check(i, j):
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 1
                    total += g[x][y]
 
                recur(cur + 1)
                
                # 다음 재귀를 위해 초기화
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 0
                    total -= g[x][y]
 
n = int(input())
g = [list(map(int, input().split())) for i in range(n)]
 
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
 
visited = [[0] * n for i in range(n)]
answer = 99999999
total = 0
recur(0)
print(answer)
#내가 풀다 만거
# def check(arr,min_price):
#     exist=[[0 for _ in range(n)] for _ in range(n)]
#     print (exist)
#     price=float("inf")
#     for i in range(1,len(arr)):
#         pass
#     return min(min_price,price)
# def alive(exist,i,j):
#     if exist[i][j]==0 and exist[i][j-1]==0 and exist[i][j+1]==0 and exist[i-1][j]==0 and exist[i+1][j]==0:
#         return True
#     else:
#         return False
# input=sys.stdin.readline
# n=int(input())
# flower=[list(map(int,input().split())) for _ in range(n)]
# result=float("inf")
# for i in range(1,n-1):
#     for j in range(1,n-1):
#         pass
