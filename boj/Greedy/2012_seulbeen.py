# 자기 예상보다 등수가 높아도 불만도를 가지는건가..?
# 1 2 3 4 5 => 전체 실제 등수(n까지의 합)
# 1 5 3 1 2 => 예측 등수
# 1 1 2 3 5 로 배치하면 최소 => 3 => 오름차 정렬해서 차이 구하면 최소?

import sys
input=sys.stdin.readline
n=int(input())
rank=[]
for _ in range(n):
    rank.append(int(input()))
rank.sort()
result=0
for i in range(n):
    result+=abs(rank[i]-(i+1))
print(result)

#원래 그냥 위처럼 한꺼번에 예측과 실제의 총합구해서 뺴려했는데 그런 케이스에 대한 반례 
#1 2 3 4
#1 1 4 4