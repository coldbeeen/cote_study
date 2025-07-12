# 블로그
# 37분
"""
슬라이딩 윈도우인거 같은데,,, 그 어려운 버전 슬라이딩 윈도우인가?

근데 기억을 더듬어 코드를 짜다보니까 
그떄는 최댓값을 찾는것이고 지금은 윈도우의 합이 최대인것을 찾는것
굳이 그 방식으로 안풀어도될듯
"""

# from collections import deque
import sys
input=sys.stdin.readline
N,X=map(int,input().split())
blog=list(map(int,input().split()))

cur_total=sum(blog[:X])
cnt=1
total=cur_total


for i in range(X,N):
    #윈도우 이전 값빼고, 현재값 추가하고
    cur_total+=blog[i]-blog[i-X]
    
    if cur_total>total:
        total=cur_total
        cnt=1
    elif cur_total==total:
        cnt+=1
if total==0:
    print('SAD')
else:
    print(total)
    print(cnt)
# total=0
# for idx,val in enumerate(blog):
#     if idx < X - 1:
#         total += val
#         continue

#     while q and blog[q[-1]]<val:
#         total-=blog[q[-1]]
#         total
#         q.pop()
#     q.append(idx)
#     if q[0]<idx-X+1:
#         q.popleft()
