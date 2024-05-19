#구글링
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

stuff = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)] # N+1 x K+1 크기로 dp행렬 구성, N=1일때도 [i-1][j]가 존재하도록 하기 위함

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= stuff[i - 1][0]: #j가 물건의 무게보다 클 때만 진행해야됨
            dp[i][j] = max(stuff[i - 1][1] + dp[i - 1][j - stuff[i - 1][0]], dp[i - 1][j])
            #해당 물건을 넣기 전의 가치 + 해당 물건의 가치 VS 직전 물건까지의 가치
        else: #j 인덱스에는 해당 무게의 물건이 못 들어감
            dp[i][j] = dp[i - 1][j] #직전 물건까지의 가치로 그대로 할당 
            
print(dp[N][K])

#백트래킹으로 푸니까 시간초과
#O(N log N)도 안 된다는 얘기인데..
#DP로 풀어야 할 듯?