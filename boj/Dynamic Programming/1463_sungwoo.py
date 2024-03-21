n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):  # 2~n까지 최적의 해를 구함
    candidate_list = []  # 후보 리스트
    if i % 3 == 0:  # 3으로 나누어떨어지면 dp[i//3] 값 후보로 추가
        candidate_list.append(dp[i//3])
    if i % 2 == 0:  # 2로 나누어떨어지면 dp[i//3] 값 후보로 추가
        candidate_list.append(dp[i//2])
    candidate_list.append(dp[i-1])  # 1을 뺀 값 후보로 추가
    dp[i] = min(candidate_list) + 1  # i의 최적의 해를 구함

print(dp[n])