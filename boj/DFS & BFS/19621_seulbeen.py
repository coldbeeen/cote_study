# 구글링함.. dp 처음 접하고 충격먹었습니다... 
import sys
input=sys.stdin.readline
n = int(input())

#회의정보 리스트 입력
meeting=[[0,0,0]]+[list(map(int,input().split())) for _ in range(n)]

# 입력이 오름차순으로 주어져있지 않을 가능성 있으므로 정렬(시작시간/종료시간 둘중 뭘로 해도 상관없음)
meeting.sort()

dp=[0 for _ in range(n+1)]

#첫 번째 인덱스에 첫 회의 인원수 저장
dp[0]=meeting[0][2]

for i in range(1,n+1):
    # max(a,b) => a : 바로 전타임의 회의가 진행 중인 경우, b : 그렇지 않아서 현재 회의를 진행할 수 있는 경우. a와 b의 대소를 비교해서 현재 회의를 진행할지, 진행하지 않고 이전 회의 진행이 이득인지
    dp[i]=max(dp[i-1],dp[i-2]+meeting[i][2])

print(dp[n])

"""
6
10 40 80
30 60 60
50 80 70
70 100 100
90 120 40
110 140 50

[80,60,70,100,40,50]

dp[80,80,150,180,190,230]
"""
# 아래는 원래 백트래킹으로 풀려다가 실패한것
# input=sys.stdin.readline

# def DFS(idx,cnt):
#     global total
#     if not visit[idx]:
#         visit[idx]=True

#         for node in graph[idx]:
#             if not visit[node]:
#                 if 0<node-1:
#                     visit[node-1]=True
#                 if node+1<=n:
#                     visit[node+1]=True
#                 cnt+=people[node]
#                 DFS(node,cnt)
#                 total=max(total,cnt)
#                 cnt-=people[node]
#                 if 0<node-1:
#                     visit[node-1]=False
#                 if node+1<=n:
#                     visit[node+1]=False
#         visit[idx]=False


# n=int(input())

# meeting=[[0,0,0]]+[list(map(int,input().split())) for _ in range(1,n+1)]
# meeting.sort(key=lambda x:(x[:][1]))

# graph=[[]for _ in range(n+1)]
# people=[0 for _ in range(n+1)]
# visit=[False for _ in range(n+1)]
# total=0
# cnt=0
# result=float("-inf")
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i!=j and j+1!=i and j-1!=i:
#             graph[i].append(j)
# for i in range(1,n+1):
#     people[i]+=meeting[i][2]

# for i in range(1,n+1):
#     total=0
#     result=max(result,DFS(i,people[i]))
# print(result)



