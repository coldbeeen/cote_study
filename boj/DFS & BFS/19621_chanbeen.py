import sys

input = sys.stdin.readline

def DFS(v, cnt):
    global result
    
    result = max(result, cnt) #result 갱신
    
    visited[v] = True
    
    for n in graph[v]:
        if not visited[n]:
            DFS(n, cnt + room[n][2]) #room[n][2] : 회의 인원
            visited[n] = False #백트래킹

N = int(input())

room = []

for _ in range(N):
    info = list(map(int, input().split()))
    
    room.append(info)

room = sorted(room, key = lambda x : x[1]) #회의가 끝나는 시간대로 정렬
#회의실 배정 1에서도 끝나는 시간순으로 정렬했었음

graph = [[] for _ in range(N)]

check = [False] * (N) #DFS 시작점들을 찾아주기 위한 배열

for i in range(N):
    for j in range(N):
        if room[i][1] <= room[j][0]:
            graph[i].append(j)
            check[j] = True #연결되어 있다는 뜻이니까 여기부터 시작할 필요 없음

visited = [False] * (N)
result = 0

for i in range(N):
    if not check[i]: #연결 요소가 없으니까 i부터 시작해야됨
        DFS(i, room[i][2])

print(result)