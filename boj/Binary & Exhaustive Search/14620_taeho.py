# 백트래킹 구글링
def check(a, b):
    for i in range(5):
        x = a + di[i]
        y = b + dj[i]
        if visited[x][y] == 1:
            return False
    return True
 

def recur(cur):
    global total, answer
    
    # 종료 조건
    if cur == 3:
        answer = min(answer, total)
        return
	
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if check(i, j):
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 1
                    total += g[x][y]

                recur(cur + 1)
                
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 0
                    total -= g[x][y]


if __name__ == "__main__":
    n = int(input())
    g = [list(map(int, input().split())) for i in range(n)]

    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]

    visited = [[0] * n for i in range(n)]
    answer = 2147000000
    total = 0
    recur(0)
    print(answer)

'''
# DFS 사용
import sys

def check(i, j, visited):
    for idx in range(4):
        ni = i + d[idx][0]
        nj = j + d[idx][1]
        if (ni, nj)  in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer:return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                if check(i, j, visited) and (i, j) not in visited:
                    temp = [(i, j)]
                    temp_cost = fields[i][j]
                    for idx in range(4):
                        ni = i + d[idx][0]
                        nj = j + d[idx][1]
                        temp.append((ni, nj))
                        temp_cost += fields[ni][nj]
                    dfs(visited + temp, total + temp_cost)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer = int(1e9)
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dfs([], 0)

print(answer)
'''