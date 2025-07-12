#N번째 큰수
# 40분
"""
우선순위 큐라는 것을 구글링...
의문점 : 메모리때문에 우선순위 큐라는 것은 알겠음, 그러나 그것이 문제의 조건(어떤 수는 바로 위 수보다 크다)와 무슨 상관..? 조건이 없어도 똑같은거 아닌가 그럼
"""
import heapq
import sys

input=sys.stdin.readline
q=[]
N=int(input())
for _ in range(N):
    nums=list(map(int,input().split()))
    for n in nums:
        if len(q)<N:
            heapq.heappush(q,n)
        else:
            if q[0]<n:
                heapq.heappop(q)
                heapq.heappush(q,n)
print(q[0])