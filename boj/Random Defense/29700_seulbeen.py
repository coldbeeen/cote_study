# 우당탕탕 영화예매
"""
슬라이딩 윈도우로 싹 탐색하면 되나?
삼중반복은 역시 시간초과가 발생...

전체 좌석을 탐색하면서 연속으로 빈좌석수를 세다가 k명이 앉을수있는 순간 답을 +1 해주고,
그 다음에도 빈좌석이 하나나올때마다 +1해주면됨
4자리에 3명이 연속으로 앉는 경우는 123, 234니까
"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
seats = list((input().rstrip()) for _ in range(n))

total = 0
# print(seats)

for i in range(n):
    # 연속된 빈자리의 수를 세는 cnt변수
    cnt = 0
    for j in range(m):
        # 빈자리라면 cnt+=1
        if seats[i][j] == "0":
            cnt += 1
        # 이미 예매된좌석이라면 다시 cnt 초기화
        else:
            cnt = 0

        # k개이상의 빈자리가 나올때마다 +1해주면됨
        if cnt >= k:
            total += 1


print(total)
