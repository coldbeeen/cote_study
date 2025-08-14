# 요세푸스 문제
# 40분
# 출력 형식이 와이리 까다롭냐

import sys
from collections import deque

input=sys.stdin.readline

n,k=map(int,input().split())
q=deque()

perm=list(i for i in range(1,n+1))
# print(perm)
idx=0

while perm:

    # 해당 인덱스 부터 카운트 하므로 k-1만 더 세면 됨
    idx+=(k-1)

    # %로 나머지 관리
    n=len(perm)
    idx%=n
    
    #해당 위치의 숫자를 pop한 후 q에 저장
    q.append(perm.pop(idx))


# 출력
print("<",end="")
for i in range(len(q)):
    if i==len(q)-1:
        print(q[i],end="")
        continue
    print(f"{q[i]}, ",end="")
print(">")
