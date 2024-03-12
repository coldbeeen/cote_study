import sys

input = sys.stdin.readline

T = int(input())

num = [1, 2, 3]

for _ in range(T):
    n = int(input())
    
    dp = [0] * (11) #n이 몇 가지 경우의 수를 가지는지 저장하는 배열, n은 11까지
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
                
    
    print(dp[n])
    
# dp[i - 1] : 1을 더해서 i가 되는 경우의 수
# dp[i - 2] : 2를 더해서 i가 되는 경우의 수
# dp[i - 3] : 3을 더해서 i가 되는 경우의 수
# 다 더해주면 됨