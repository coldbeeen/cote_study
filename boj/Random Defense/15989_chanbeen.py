#약 15분 소요

T = int(input())

dp = [1] * 10001 #최대 입력 정수는 1만

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(T):
    n = int(input())

    print(dp[n])

#점화식 세워서 dp로 푸는 문제
#1만 사용하여 n을 만드는 경우의 수는 모든 n이 1가지씩 가지고 있으므로, 값 1로 초기화
#n - 2에서 2를 더하면 n이 되므로 dp 리스트 내 값 업데이트
#같은 방식으로 3도 업데이트 적용 