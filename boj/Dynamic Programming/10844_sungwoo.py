n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]  # n X 10 리스트 생성
dp[0] = [0,1,1,1,1,1,1,1,1,1]  # 1의 자릿수에 대한 dp값을 설정 (각각 0~9로 끝나는 계단 수의 개수)

for i in range(1, n):  # 1부터 시작 (2의 자릿수부터 시작)
    for j in range(10):  # 0~9로 끝나는 계단 수의 개수를 구함
        # i-1 자릿수의 dp값을 활용함
        # j로 끝나는 계단수는 i-1 자릿수의 계단수 중 j-1로 끝나는 계단수 개수 + j+1로 끝나는 계단수 개수로 구해짐
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n-1]) % 1000000000)