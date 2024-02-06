# 런타임에러(Recursion Error) 떠서 구글링 해본 결과
# 파이썬의 기본 재귀 한계는 1000쯤인데, 이 문제는 그걸 살짝 넘는다고 해서 sys.setrecursionlimit(2000) 을 추가했더니 맞았다고 뜸

import sys
input=sys.stdin.readline
sys.setrecursionlimit(2000)
t=int(input())
def search(idx):
    global cnt
    if visit[idx]: #이미 방문한, 즉 탐색시작 지점을 한번 더 왔을때 싸이클이라고 판단하고 cnt 증가
        cnt+=1
    else: # 방문하지 않은 곳일 때
        visit[idx]=True
        search(graph[idx])    
            
for _ in range(t):
    cnt=0
    n=int(input())
    graph=list(map(int,input().split()))
    graph.insert(0,0)
    visit=[False for _ in range(n+1)]
    
    for i in range(1,len(graph)):
        if visit[i]==False: #이미 싸이클의 일부분(이미 재귀함수에서 방문했던 곳)이면 검사할 필요가 없음
            search(i)
    
    print(cnt)
