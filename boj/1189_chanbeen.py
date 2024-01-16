import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())

route = [list(input().rstrip()) for _ in range(R)]
#visited = [[0] * C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 서 동 남 북

def comebackhome(x, y, cnt):
    global ans
    
    if x == 0 and y == C - 1 and cnt == K:
        ans += 1
        return
    
    for i in range(4): #동 서 남 북
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and route[nx][ny] == '.': #visited 조건문이 앞에 있으면 IndexError 뜸
            route[nx][ny] = 'T'
            comebackhome(nx, ny, cnt + 1)
            route[nx][ny] = '.'

ans = 0

route[R - 1][0] = 1
comebackhome(R - 1, 0, 1) #초기 위치

print(ans)

#visited로 만들어서 0과 1로 관리해봤는데 얘는 계속 예제 출력이 10이 나옴
#반면 그냥 입력받은걸 그대로 써서 방문한 곳을 'T', 방문안한 곳을 '.'으로 처리했더니 맞게 나옴, 왜 이런 결과가 나왔을까?