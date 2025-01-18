# 64분
# x+n
# x*2
# x*3
# 거꾸로 하려했는데 아닌 케이스가 너무 많음
# dfs 하려다가 구현 못하고 dp로 함
def solution(x, y, n):
    max_num = 1000000

    dp = [max_num for _ in range(y + 1)]

    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == max_num:
            continue
        # i를 더하는 행위(+1)
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        # 2를 곱해 만드는 행위(+1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        # 3을 곱해 만드는 행위(+1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    if dp[y] == max_num:
        return -1

    return dp[y]
