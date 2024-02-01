import sys

team_num = int(input())
l = list(map(int, sys.stdin.readline().split()))
l.sort()  # 정렬 먼저!

i = 0
result = float('inf')  # 최소값을 구하기 위해 무한대로 설정 (혹은 max(l)로)
while i < team_num:
    opposite_i = -(i+1)  # 반대편 인덱스
    s = l[i] + l[opposite_i]
    if s < result:
        result = s

    i += 1

print(result)