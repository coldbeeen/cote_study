import sys

input = sys.stdin.readline

N = int(input())
A_list = [0] + list(map(int, input().split()))

dp = [0] + [1] * 1000 #길이를 저장하는 수열
#각자 자신이 부분 수열의 길이가 될 수 있으니까 초기화 값을 1로 설정

for i in range(2, N + 1):
    for j in range(1, i): #이전 인덱스와 비교를 하면서
        if A_list[i] > A_list[j]: #더 큰 수가 등장했을 때
            dp[i] = max(dp[i], dp[j] + 1) #i번째 인덱스에서 형성되는 부분 수열의 길이 갱신

print(max(dp))