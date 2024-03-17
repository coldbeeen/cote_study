n, m = map(int, input().split())

dp = [1 for _ in range(n+1)]  # 팩토리얼을 담기 위한 DP 테이블

for i in range(2, n+1):  # 팩토리얼 계산
    dp[i] = dp[i-1] * i

result = dp[n] // (dp[m] * dp[n-m])  # nCr 공식 (아래 주석 참고)
print(result)

# N // D가 아닌 int(N/D)을 계산할 경우 틀렸습니다가 나옴
# 파이썬에서 int는 크기 제한이 없으나 float는 그렇지 않기 때문에, 결과값이 아주 클 경우 오차가 발생할 수 있다고 함