import sys
input=sys.stdin.readline

n=int(input())

dp=[]

for _ in range(n):
    dp.append(list(map(int,input().split())))

# 이전 집의 대각선 dp값에서 가장 작은 것에 현재 dp를 더해감 (사용하지 않은 색)
for i in range(1,n):
    for j in range(3):
        if j==0:
            dp[i][j]+=min(dp[i-1][j+1],dp[i-1][j+2])
        elif j==2:
            dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j - 2])
        else:
            dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j + 1])

# 마지막 행 : 마지막 집을 무슨 색으로 칠하냐에 따른 최소비용들이 담겨있고, 그중에 가장 작은 값 출력
print(min(dp[n-1]))