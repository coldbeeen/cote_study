from itertools import permutations

n = int(input())
scv = list(map(int, input().split())) + [0, 0]

# DP 테이블 생성 - 각 경우의 수(체력)에 도달하기 위한 횟수를 저장하기 위해 각 SCV 체력으로 3차원 리스트 생성
dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 0  # 시작 지점 횟수 초기화 (0회)

combs = list(permutations([9, 3, 1], 3))
for x in range(scv[0], -1, -1):
    for y in range(scv[1], -1, -1):
        for z in range(scv[2], -1, -1):
            if dp[x][y][z] > -1:  # 0 이상의 값이라면 (횟수가 갱신되고 있는 경우의 수들만 고려))
                for comb in combs:  # 모든 공격을 시도
                    nx = x - comb[0] if x - comb[0] >= 0 else 0
                    ny = y - comb[1] if y - comb[1] >= 0 else 0
                    nz = z - comb[2] if z - comb[2] >= 0 else 0

                    # 아직 횟수가 초기화되지 않았거나 기존 횟수보다 더 적은 횟수로 공격할 수 있다면 갱신
                    if dp[nx][ny][nz] == -1 or dp[nx][ny][nz] > dp[x][y][z] + 1:
                        dp[nx][ny][nz] = dp[x][y][z] + 1

print(dp[0][0][0])  # 각 SCV 체력이 0, 0, 0에 도달하기까지의 공격 횟수