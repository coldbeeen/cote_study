import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

dp = [0] * (100000 + 1) #동전 가치가 100000까지이므로

for i in range(len(coin)):
    dp[coin[i]] += 1 #본인 자체가 하나의 경우의 수가 됨
    
    for j in range(coin[i] + 1, k + 1):
        if dp[j - coin[i]] != 0:
            dp[j] += (dp[j - coin[i]]) #경우의 수 누적합

print(dp[k])

# 예시
# 0  1  2  3  4  5  6  7  8  9  10     인덱스 (k)
# 0  1  1  1  1  1  1  1  1  1  1      동전 가치 : 1
# 0  1  2  2  3  3  4  4  5  5  6      동전 가치 : 2
# 0  1  2  2  3  4  5  6  7  8  10     동전 가치 : 5