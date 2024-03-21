import sys

input= sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [1 for _ in range(n)] # 그 자신도 카운팅하므로 초기값은 1

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            # 기준이 되는 숫자 앞의 배열들과 비교하며 현재값이 더 클 경우 dp값 갱신
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))