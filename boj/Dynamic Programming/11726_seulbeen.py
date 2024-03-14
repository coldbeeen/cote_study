# 결국 n을 1과2의 합으로 나타내는 경우의 수인가?
# 5= 1 1 1 1 1, 2 1 1 1 , 1 2 1 1, 1 1 1 2, 1 2 2 , 1 2 1, 2 1 2, 
import sys

input=sys.stdin.readline
n=int(input())

dp=[0] * (n+1)
dp[0]=1
dp[1]=1

for i in range(2,n+1):
    #(i-1)에서 1을 더하는 경우의 수 + i-2에서 2를 더하는 경우의 수
    dp[i]=dp[i-1]+dp[i-2]

#문제 조건에 맞게 출력
print(dp[n]%10007)