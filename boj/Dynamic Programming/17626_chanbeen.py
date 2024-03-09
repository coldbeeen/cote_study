import sys
import math

input = sys.stdin.readline

n = int(input())

limit = 50000
dp = [0] * (limit + 1) #N은 50000까지, 제곱수 합 개수를 배열에 저장

dp[1] = 1 #초기값

for i in range(2, n + 1):
    dp[i] = 5 #모든 자연수는 4개 이하의 제곱수의 합으로 표현 가능
    
    for j in range(1, int(math.sqrt(i)) + 1): #j 범위 : 1 ~ (루트 i)
        idx = i - j *j
        
        if idx >= 0: #조건 : 직전 수(dp[idx])에서 j의 제곱을 더하면 i로 도착할 수 있는가?
            dp[i] = min(dp[i], dp[idx] + 1)
    
print(dp[n])

#pypy3로는 통과, python3로는 시간 초과
#이게 최선인 거 같은데.. 1중 반복문으로 이 문제를 풀 수 있나?