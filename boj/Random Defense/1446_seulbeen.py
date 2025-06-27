# 지름길
# 56분

"""
알고리즘 분류에 다익스트라로 되어있어서 오히려 애먹음...
dp가 더 쉬울거같은데 라는 생각이 들어서 중간에 dp로 바꿈
"""
import sys

input = sys.stdin.readline

N, D = map(int, input().split(" "))

# 지름길 배열
shortcut = []

# 도로배열
road = [i for i in range(D + 1)]

for _ in range(N):
    s, e, d = map(int, input().split(" "))
    # 문제 예시 1번처럼, 지름길인줄 알았던 길이 오히려 더 긴 경우가 있음. 그것을 필터링
    if e - s > d:
        shortcut.append((s, e, d))
shortcut.sort()

# print(shortcut)


for s, e, d in shortcut:
    for i in range(1, D + 1):
        # 지름길의 목적지에 해당하는 좌표라면, 지름길을 타는것이 이득일지 판단
        if i == e:
            road[i] = min(road[s] + d, road[i])
        # 그냥 일반 좌표라면, 그 전길에 +1을 추가하는 정상루트가 이득인지 판단
        else:
            road[i] = min(road[i - 1] + 1, road[i])
print(road[D])
