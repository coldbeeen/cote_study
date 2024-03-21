n = int(input())
l = list(map(int, input().split()))
dp = [0 for _ in range(n)]  # dp 테이블 생성
dp[0] = l[0]  # 첫 번째 값 초기화

for i in range(1, n):
    dp[i] = max(dp[i-1] + l[i], l[i])  # 앞서 누적된 합 중 가장 큰 값과 l[i]를 비교해 큰 값으로 dp[i] 설정

print(max(dp))  # 가장 큰 값 선택