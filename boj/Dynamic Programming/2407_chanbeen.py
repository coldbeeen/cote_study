import sys

sys.stdin.readline

n, m = map(int, input().split())

dp = [0] * 101
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] * i #팩토리얼 저장
    
print(int(dp[n]//(dp[n - m] * dp[m])))
    
# 4%에서 틀린다?
# 예시가 잘 나오는걸 보니 수식 문제는 아님
# 알고 보니, //를 써야하는 것이었음, /를 쓰면 틀림
# 파이썬에서 int는 크기 제한이 없으나 float는 아니라서, 결괏값이 매우 커지면 오차가 발생할 수 있다고 하네요