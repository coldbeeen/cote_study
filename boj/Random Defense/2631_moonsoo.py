import sys

input = sys.stdin.readline

N = int(input())

children = []
for _ in range(N):
    child = int(input())
    children.append(child)

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(0, i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(len(children) - max(dp))