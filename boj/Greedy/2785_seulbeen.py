import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
chain=deque(sorted(list(map(int,input().split())))) # 정렬해서 체인을 뜯어서 이어줘야하니 데크를 채용했음
cnt=0
while len(chain)>1:
    chain[0]-=1 # 첫 체인(가장 작은 체인) 고리를 뜯음
    tmp=chain.pop()
    chain[-1]+=tmp # 제일 긴 체인과 그 다음으로 긴 체인을 아까 뜯은 고리로 연결
    cnt+=1 
    if chain[0]==0: #가장 짧은 체인 뜯었을 때 0이면 pop해줘야지 (고리가 없응께)
        chain.popleft()
print(cnt)
# 궁금증: line 9,10을 chain[-1]+=chain.pop()로 했는데 시간 소요가 600 -> 3900으로 늘음. 왜그러지?? 오히려 가벼워져야되는거 아닌가...