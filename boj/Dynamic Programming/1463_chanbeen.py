import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)

for i in range(2, N + 1): #1을 만들어야 되므로 2부터 시작해야 됨
    dp[i] = dp[i - 1] + 1 #1을 빼는 경우
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1) #3으로 나누어 떨어지는 경우
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1) #2로 나누어 떨어지는 경우

print(dp[N])