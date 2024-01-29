import sys
input=sys.stdin.readline
t=int(input())
def Search(idx):
    global cnt # 최소숫자 전역변수
    if visited[idx]==True: # 방문했던 애로 돌아오면 무한 반복되므로 실패(그전에 못 만난거면 평생 못만남)
        print('0')
        return
    if idx==n: # 친구가 걸리게 하는데 성공하였다면 cnt 출력 후 return
        print(cnt)
        return
    visited[idx]=True # 방문표시 갱신
    cnt+=1 #cnt 증가
    Search(graph[idx]) # 현재 사람이 가리키고 있는 사람한테 함수 재귀호출

for _ in range(t):
    n=int(input())
    cnt=0
    graph=[0 for _ in range(n+1)]
    visited=[False for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i]+=int(input())
    Search(1)