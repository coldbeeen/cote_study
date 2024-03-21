import sys

input= sys.stdin.readline

n, m = map(int, input().split())

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i < j:
            # nCm에서 n<m인 경우는 정의되지 않으므로 0으로 초기화된 채로 넘어간다
            continue
        
        elif j == 1:
            # nC1 = n
            dp[i][1] = i
        
        else:
            # nCm = n-1Cm-1 + n-1Cm
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]


print(dp[n][m])

"""
문제:

nCm 출력
______________________________________________________________________
풀이:

nCm = n-1Cm-1 + n-1Cm 과 같다.
아래서부터 차례로 올라가면 된다.
"""