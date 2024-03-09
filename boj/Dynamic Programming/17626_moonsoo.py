import sys
import math
input= sys.stdin.readline

n = int(input())

dp = [4] * 50001 # 모두 최대 개수인 4로 초기화
for N in range(1, n + 1):
    if math.sqrt(N) % 1 == 0:
        # 어떤 수의 제곱근이라면
        dp[N] = 1
    else:
        for i in range(1, N//2 + 1):
            dp[N] = min(dp[N], dp[i] + dp[N - i])

            if dp[N] == 2:
                # 2만 찾아도 최소이기 때문에 불필요한 실행 없애기
                break


print(dp[n])