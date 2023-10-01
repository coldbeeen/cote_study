import sys

input = sys.stdin.readline

N = int(input())

rank = [int(input()) for i in range(N)]

rank.sort()

result = 0

for i in range(N):
    result += abs(rank[i] - (i + 1))
    #|예측 등수 - 실제 등수|

print(result)