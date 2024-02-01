import sys
input=sys.stdin.readline
n=int(input())
link=int(input())
graph=[[] for _ in range(n+1)]
visit=[False for _ in range(n+1)]
visit[1]=True # 1번은 무조건 감염
cnt=0
def search(idx):
    # 종료조건이 뭐지
    # 딱히 없어도 되네?
    # 어차피 for문이 끝나면 함수가 끝나니 재귀함수의 일반적인 형태처럼 탈출조건이 없어도 되는듯
    global cnt
    for node in graph[idx]: # 각 컴퓨터에 연결된 컴퓨터들을 탐색하며 재귀호출
            if visit[node]==False:
                cnt+=1
                visit[node]=True
                search(node)

for i in range(1,link+1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
search(1)

print(cnt)
#1: [2,5]
#2: [1,3,5]
#3: [2]
#4: [7]
#5: [1,2,6]
#6: [5]
#7: [4]