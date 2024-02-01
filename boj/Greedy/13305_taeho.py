# 기름 싼데서 최대한 많이 주유해야함
# 

import sys
input = sys.stdin.readline

N = int(input())

roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

# 제일 싼 집
min_cost = costs[0]

# 맨 처음 값
min_price = roads[0] * costs[0]

for i in range(1, N-1):
  if min_cost > costs[i]: # 지금 주유소가 더 싸면,
    min_cost = costs[i] # 지금 주유소로 변경
  
  min_price += min_cost * roads[i] # 최소비용 = 비용 * 현재 거리

print(min_price)