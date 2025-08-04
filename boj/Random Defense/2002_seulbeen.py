# 추월
# 21분
"""
구현 문제
"""
import sys
from collections import defaultdict, deque

input=sys.stdin.readline

n=int(input())

# 터널 진입순서대로 차량번호에 매핑
tunnel=defaultdict(int)

# idx==현재 들어와야 하는 차량의 번호
idx=0
cnt=0

for i in range(n):
    car=input().rstrip()
    tunnel[car]=i
# print(tunnel)

# 터널 진출 차량 
out=deque()
# 차량이 진출했다면 집합에서 제거해줄것
check=set([i for i in range(len(tunnel))])
for i in range(n):
    out.append(input().rstrip())
# print(out)

while out:
    o=out.popleft()

    # 터널 진출 차량의 번호와 현재 인덱스가 일치한다면 Idx+=1
    if idx==tunnel[o]:
        idx+=1
    
    # 그렇지 않을경우
    else: # if idx != tunnel

        # 현재 인덱스 차량보다 늦게 나와야 하는 차량이 남은 대기열 차량들보다도 빠르게 나온것이라면 추월
        if tunnel[o]>min(check):
            cnt+=1
    check.remove(tunnel[o])
    # print(check)

    

print(cnt)
