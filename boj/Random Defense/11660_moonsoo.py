N, M = map(int, input().split())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for r in range(1, N + 1):
    nums = list(map(int, input().split()))
    
    for c in range(1, N + 1):
        dp[r][c] = nums[c-1] + dp[r-1 if r-1>=0 else 0][c] + dp[r][c-1 if c-1>=0 else 0] - dp[r-1 if r-1>=0 else 0][c-1 if c-1>=0 else 0]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

"""
문제:
N×N의 매트릭스가 주어지고 M개의 (x1, y1)부터 (x2, y2)까지의 합을 구하기.
------------------------------------------------------------------------------------------------
풀이:
시간이 1초로 제한되어 있는 것을 보아 완전탐색으로의 접근은 시간 초과가 난다.
따라서 DP로 접근하였는데 2차원 DP 배열을 만들어 dp[x][y] = (x,y)까지의 합으로 정의한다.

이 때, (x1, y1)부터 (x2, y2)까지의 합은 dp[x2][y2]에서 dp[x2][y1-1], dp[x1-1][y2]를 빼고 중복해서 빠진 dp[x1-1][y1-1]을 더해준다.
DP를 사용하면 M이 몇개가 주어지든 선형시간에 계산이 끝나기 때문에 최악의 경우에도 O(M)안에 끝난다.

그래도 시간 초과가 계속 나서 값을 입력받는 동시에 바로 DP 배열로 만들어주었으나 이 경우에도 시간 초과가 났다.
PyPy3로 제출해서 해결.
"""