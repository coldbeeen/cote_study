import sys

input = sys.stdin.readline

n = int(input())

wine = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)

dp[1] = wine[1]

if n != 1:
    dp[2] = dp[1] + wine[2]
    
for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i], dp[i - 1])

print(max(dp))

#계단 오르기와 거의 같은 문제
#기본 점화식 : A[i] = max(A[i - 3] + wine[i - 1] + wine[i], A[i - 2] + wine[i])
#그러나 와인양이 음이 아닌 정수이므로 0도 가능하다는 것이 차이점
#0이 2번 연속 등장하면 기본 점화식의 경우 이전 dp값이 계승이 안 됨
#따라서 0이 계속 등장해도 dp값을 계승시켜줄 수 있도록 기본 점화식을 약간 변경
#변형 점화식 : A[i] = max(A[i - 3] + wine[i - 1] + wine[i], A[i - 2] + wine[i], A[i - 1])
#0이 등장하면 그냥 이전 값을 그대로 계승하는 구조