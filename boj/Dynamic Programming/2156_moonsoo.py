import sys

n = int(sys.stdin.readline())
drink = [0] + [int(sys.stdin.readline()) for _ in range(n)]

dp = [0, drink[1], drink[1] + drink[2] if n>1 else None]

for i in range(3, n + 1):
    result = max(dp[i-2] + drink[i], dp[i-3] + drink[i-1] + drink[i], dp[i-1])
    dp.append(result)

print(dp[n])

"""
문제:

최대로 마실 수 있는 경우 구하기. 연속 세 번은 불가.
_________________________________________________
풀이:

이전에 했던 계단 문제와 유사.
처음에는 dp[n]을 n번째를 선택하면서 최대가 되는 값으로 하려했으나
n번째까지 고려하더라도 n을 포함하지 않고 최대가 되는 경우가 있는 것을 알게 됨.
따라서 max() 안에 dp[n-1]까지와의 비교도 포함해주었다.

indexerror가 난 부분에 대해서는 dp 배열을 2번 인덱스까지 초기화해주었는데 n=1일 경우, 2번 값을 조회할 수가 없음
따라서 n>1일 때만 넣어주는 것으로 해결했다.
그런데 이렇게 하는 게 최선인가..?
"""