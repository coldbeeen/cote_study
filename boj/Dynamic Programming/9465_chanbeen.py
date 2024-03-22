import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    dp = [[0] + list(map(int, input().split())) for _ in range(2)]
    
    for i in range(2, n + 1):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    
    print(max(dp[0][n], dp[1][n]))
    
# 앞에서 채워나가는 게 아니라 뒤에서부터 뭘 골랐을까 생각해보면 이해가 더 잘 됨
# 해당 칸의 스티커는 무조건 사용하므로 이전 칸에서는 같은 행의 스티커를 사용하지 않은 것
# 다른 행의 스티커도 하나를 사용하면 양 옆의 스티커는 사용하지 못 함
# 따라서, 다른 행의 스티커 중 이전 열 또는 이전이전 열의 스티커 중 높은 점수를 가진 스티커를 사용해주면 된다

# dp 배열에는 해당 행, 열에서 가질 수 있는 가장 큰 점수값이 들어감 
# 따라서 마지막 열에 있는 두 값 중 더 큰 값을 출력하게 하면 됨