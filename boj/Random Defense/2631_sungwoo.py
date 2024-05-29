n = int(input())
num_list = [int(input()) for _ in range(n)]
dp = [1 for _ in range(n)]  # DP 테이블. 기본값 1로 설정

for i in range(1, n):
    for j in range(i):  # 인덱스 i의 앞 부분을 순회하며
        if num_list[j] < num_list[i]:  # 인덱스 i보다 값이 더 작은 인덱스 j에 대해서
            dp[i] = max(dp[i], dp[j] + 1)  # 가장 큰 DP 값(i 이전 인덱스까지의 LIS) + 1로 DP 테이블 업데이트

len_of_LIS = max(dp)  # 최댓값이 가장 긴 증가하는 부분 수열의 길이
print(n - len_of_LIS)  # LIS 요소값들을 제외한 나머지를 적절히 옮겨주면 최적의 이동 횟수임