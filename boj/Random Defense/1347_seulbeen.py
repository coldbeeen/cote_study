# 미로만들기
# 1시간 20분
"""
What...? 뭔가 참신해보이는 구현문제인듯...?

<막힌 부분>
시작 위치는 미정
남쪽(아래)를 보고 스타트
각 행과 열에는 적어도 이동할수있는 칸이 있음
이동할 수 있는 모든칸을 걸어 다녔음, 즉 입력받은 대로 행동하고 난 후의 나머지 칸들은 벽이었다는 소리
근데 시작 위치와 전체 크기를 몰라서 감이 안잡힘

=> 막연하게 그려보니까 굳이 시작위치를 몰라도, 자연스럽게 그려진다 ㄷㄷ

ps) 그리고, L 방향으로 가는걸 음수에 연산자 붙이는거 계산하기 귀찮았는데, 생각해보니까 R방향으로 세번 도는게 L방향으로 한번 도는 것과 동일함


"""
import sys

input = sys.stdin.readline
n = int(input())
commands = input().rstrip()

# 남 서 북 동 시계방향 배열
dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
# 방향 배열에 관한 인덱스 관리
d_idx = 0

# 문제조건에서 input길이의 최댓값은 50이므로, 가운데에서 출발한다고 가정 시 총 101*101 배열이라면 모든 움직임 커버 가능
road = [["#"] * 101 for _ in range(101)]

# 출발 위치는 정가운데
cx, cy = 50, 50
road[cx][cy] = "."

# 가운데에서 출발하고, 이동범위에 맞게 슬라이싱하여 출력하기 위한 상하좌우 경계선
l_bound, t_bound, r_bound, b_bound = 50, 50, 50, 50


# 입력 커맨드에 따른 방향전환
def change_direction(cmd):
    global d_idx
    if cmd == "L":
        d_idx += 3
    elif cmd == "R":
        d_idx += 1

    d_idx %= 4


for c in commands:

    if c == "F":
        # 전진 실행
        cx += dir[d_idx][0]
        cy += dir[d_idx][1]
        road[cx][cy] = "."

        # 경계점 갱신
        t_bound = min(t_bound, cx)
        b_bound = max(b_bound, cx)
        l_bound = min(l_bound, cy)
        r_bound = max(r_bound, cy)

    else:
        # 방향 전환
        change_direction(c)

# 범위에 맞게 미로 출력
for i in range(t_bound, b_bound + 1):
    for j in range(l_bound, r_bound + 1):
        print(road[i][j], end="")
    print()
