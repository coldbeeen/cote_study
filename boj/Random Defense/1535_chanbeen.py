#90분 +@, 구글링

N = int(input())
life = list(map(int, input().split()))
joy = list(map(int, input().split()))

life = [0] + life
joy = [0] + joy

dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1): #각 사람 순회
    for j in range(1, 101): #각 체력 순회
        if j - life[i] > 0: #이 사람 만나기 가능, joy 최댓값 갱신
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - life[i]] + joy[i])
        else: #현재 체력에 이 사람 만나기 불가능
            dp[i][j] = dp[i - 1][j]
            
print(dp[-1][-1])

#그리디인줄 알았으나, 해결 안 되는 케이스 존재
#DP로 접근
#행은 각 사람, 열은 각 체력에서 얻을 수 있는 기쁨