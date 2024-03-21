n = int(input())
dp = [float('inf') for _ in range(n+1)]  # dp 테이블 inf로 초기화

i = 1
while i**2 <= n:  # 제곱수에 대해서만 dp 테이블 1로 초기화
    dp[i**2] = 1
    i += 1

for i in range(2, n+1):  # 2부터 시작하여
    j = 1
    while j**2 <= i:  # 제곱수가 i 이하일 때까지 반복
        dp[i] = min(dp[i], dp[j**2] + dp[i-(j**2)])  # 해당 제곱수의 합 최소 개수(dp[j*j]) + i에서 해당 제곱수를 뺀 값의 합 최소 개수를 더해 최솟값 갱신
        j += 1

print(dp[n])