n = int(input())
seq = list(map(int, input().split()))

dp = [1 for _ in range(n)]  # 기본값 1로 설정

for i in range(1, n):
    for j in range(i):  # 인덱스 i의 앞부분을 순회하며
        if seq[j] < seq[i]: # 인덱스 i보다 값이 더 작은 인덱스 j에 대해서만 dp 테이블 업데이트
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # 최댓값이 곧 최대 수열의 길이