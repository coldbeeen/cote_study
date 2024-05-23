import sys

n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(n + 1)]

# 첫번째 줄은 임의로 초기화해준다.
for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = (dp[i-1][j-1] if j>0 else 0) + (dp[i-1][j+1] if j<9 else 0)

print(sum(dp[n]) % 1000000000)

"""
문제:

매 자리의 수는 전과 인접한 수 밖에 오지 못한다. N길이의 계단 수를 구해보자.
_______________________________________________________________________
풀이:

찬빈이와 이야기해보고 문제의 메모리 제한을 보니 이중배열을 써도 넉넉하겠단 생각이 들었다.
n번째에 대해 0~9까지의 경우의 수를 적고 보니

ex)
n번째 자리에 7이 오고 싶다면 n-1번째 자리에 6 혹은 8이 온 경우의 수를 더하면 된다는 것을 깨달았다.
이 때, 관건은 0과 9인데 인덱스를 벗어나는 경우는 0 처리를 해서 해결하였다.
"""