import sys
input = sys.stdin.readline

n = int(input())
pillar_list = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
pillar_list.sort(key = lambda x: x[0])  # 위치순 정렬 수행

max_height = max(pillar_list, key=lambda x: x[1])[1]  # 최대 높이 먼저 구하기 (최대 높이의 기둥을 기준으로 양 옆을 나눠 면적을 구할 것임)
area = 0

# 오른쪽으로
prev_pillar = [0,0]
for i in range(len(pillar_list)):
    cur_pillar = pillar_list[i]

    if cur_pillar[1] > prev_pillar[1]:  # 이전 기둥보다 현재 기둥이 높다면 넓이 계산 (누적)
        area += (cur_pillar[0] - prev_pillar[0]) * prev_pillar[1]
        prev_pillar = cur_pillar

        if cur_pillar[1] == max_height:  # 가장 높은 기둥이라면 해당 기둥 기록 후 종료
            left_max_pillar = cur_pillar
            break

# 왼쪽으로
prev_pillar = [0,0]
for i in range(len(pillar_list) - 1, -1, -1):
    cur_pillar = pillar_list[i]

    if cur_pillar[1] > prev_pillar[1]:  # 이전 기둥보다 현재 기둥이 높다면 넓이 계산 (누적)
        area += (prev_pillar[0] - cur_pillar[0]) * prev_pillar[1]
        prev_pillar = cur_pillar

        if cur_pillar[1] == max_height:  # 가장 높은 기둥이라면 해당 기둥 기록 후 종료
            right_max_pillar = cur_pillar
            break

area += (right_max_pillar[0] - left_max_pillar[0] + 1) * max_height  # 가장 높은 기둥의 면적까지 계산하여 누적

print(area)  # 최종 면적 출력