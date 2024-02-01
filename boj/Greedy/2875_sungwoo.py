N, M, K = map(int, input().split())

Q = N // 2

team = min(Q, M)

N -= 2 * team
M -= team

K = K - (N + M)
if K > 0:
    team -= (K-1) // 3 + 1

print(max(0, team))