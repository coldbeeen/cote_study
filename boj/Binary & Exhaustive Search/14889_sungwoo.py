from itertools import combinations

n = int(input())
s_list = [list(map(int, input().split())) for i in range(n)]

combs = combinations(range(n), n//2)
result = []

for team1 in combs:

    # team1의 능력치 합
    team1_s = 0
    for i in team1:
        for j in team1:
            if i == j:  # 같은 사람은 건너뜀
                continue
            team1_s += s_list[i][j]

    # team2의 능력치 합
    team2 = [i for i in range(n) if i not in team1]  # team1의 사람을 모두 제외한 사람
    team2_s = 0
    for i in team2:
        for j in team2:
            if i == j:  # 같은 사람은 건너뜀
                continue
            team2_s += s_list[i][j]

    # 두 팀의 능력치 합의 차를 리스트에 추가
    result.append(abs(team1_s - team2_s))

print(min(result))  # 최솟값 출력