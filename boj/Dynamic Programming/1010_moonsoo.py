import sys
input= sys.stdin.readline

T = int(input())

# m개의 오른쪽 다리 중 연결 가능한 왼쪽의 n개인 mCn을 구하는 문제
# DP적으로 접근하면 mCn = m-1Cn + m-1Cn-1

dp = [[0 for j in range(30)] for i in range(30)]
for i in range(1, 30):
    for j in range(1, 30):
        if i < j:
            dp[i][j] = -1
        
        if j == 1:
            dp[i][1] = i
        
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            
for _ in range(T):
    n, m = map(int, input().split())

    print(dp[m][n])
