import sys
sys.setrecursionlimit(10**6)

def dfs(node, t):
    t += meetings[node][2]
    if meetings[node][1] > max_start:
        result.append(t)
    for n in range(node+1, N):
        if meetings[node][1] > meetings[n][0]:
            continue
        dfs(n, t)

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[0], x[1]))
result = []
max_start = max([start for start, end, n in meetings])
for i in range(N):
    dfs(i, 0)
print(max(result))