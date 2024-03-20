import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [float("-inf")] * 100000 #n은 10만까지
dp[0] = num[0]

for i in range(1, n):
    dp[i] = max(num[i], dp[i - 1] + num[i])

print(max(dp))

#연속되는 값을 계속해서 더해나가는 게 이득인지 판단
#이득이 아니라면 자기 자신으로 dp 원소값을 할당

#52%에서 틀렸습니다?
#처음 초기화때 0으로 초기화해서 그런거였음