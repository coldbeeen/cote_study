import sys
input = sys.stdin.readline

n = int(input())
weights = sorted([int(input()) for i in range(n)])  # 우선 정렬부터!

max_weight = 0

i = 0
while i < n:
    can_lift = weights[i] * (n - i)  # 해당 무게 밧줄 (n-i)개로 들 수 있는 무게
    if can_lift > max_weight:  # 들어올릴 수 있는 최대 중량 갱신되는 조건
        max_weight = can_lift
    i+= 1

print(max_weight)








'''
5 15 10
5*3 = 15
10*2 = 20

50 20 5
5*3 = 15
20*2 = 40
50*1 = 50
'''