import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    dp = [1] * (M + 1)
    
    for i in range(2, M + 1):
        dp[i] = dp[i - 1] * i
        
    print(int(dp[-1]/(dp[M - N] * dp[N]))) #NCM 경우의 수를 구하는 문제