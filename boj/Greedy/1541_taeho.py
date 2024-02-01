# - 기준으로 괄호 쳐서
# 파트별 애들 계산해준 뒤
# 맨 처음꺼에서 전부 다 빼주면 됨

import sys
input = sys.stdin.readline

eq = input().split('-')

num = []

for i in eq:
    cnt = 0
    plus = i.split('+')

    for j in plus:
        cnt += int(j)

    num.append(cnt)

min = num[0]

for i in range(1, len(num)):
    min -= num[i]

print(min)