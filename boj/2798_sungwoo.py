import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

combs = combinations(cards, 3)  # cards 중 원소 3개의 조합 생성
result = 0
for comb in combs:  # 조합을 순회하며
    sumOfComb = sum(comb)  # 각 조합의 합이
    if sumOfComb <= m and sumOfComb > result:  # m보다 작거나 같고, result보다 크다면 갱신
        result = sumOfComb

print(result)