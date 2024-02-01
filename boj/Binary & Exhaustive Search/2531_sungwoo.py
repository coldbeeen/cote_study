import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for i in range(n)]

result = 0

for i in range(n):

    s = set()  # 집합 자료형 생성
    for j in range(k):  # i부터 i+3까지의 초밥 넣기
        s.add(belt[(i+j)%n])

    s.add(c)  # 쿠폰 초밥 넣기
    s_len = len(s)  # 집합의 길이를 구함

    if s_len > result:  # max 갱신
        result = s_len

print(result)