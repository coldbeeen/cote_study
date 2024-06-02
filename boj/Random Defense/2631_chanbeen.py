#마감 기한 초과
import sys

input = sys.stdin.readline

N = int(input())

kid = [int(input()) for _ in range(N)]

dp = [1] * (N)

for i in range(1, N): #LIS 알고리즘
    for j in range(i):
        if kid[j] < kid[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))

#LIS : 가장 긴 증가하는 부분 수열 문제
#이미 정렬되어 있는 아이들을 카운트한 후, 전체 명 수에서 빼주면 됨
#정렬이 안 되어있는 아이들만 정렬을 시키면 되기 때문