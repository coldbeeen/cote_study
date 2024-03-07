import sys

input = sys.stdin.readline

N = int(input())

bag = [3, 5] #3kg, 5kg

limit = 5000 #N은 5000까지
dp = [limit + 1] * (limit + 1)

dp[0] = 0

for i in range(len(bag)): #3kg와 5kg를 사용해서 N의 위치로 갈 수 있는지 테스트
    for j in range(bag[i], N + 1):
        if dp[j - bag[i]] != limit + 1: #이전 위치에 값이 할당되어있다면
            dp[j] = min(dp[j], dp[j - bag[i]] + 1) #현재 위치로 올 수 있으므로 값 갱신
            
print(dp[N] if dp[N] != limit + 1 else -1) #값 갱신이 된 적 없으면 -1 출력