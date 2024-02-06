import sys
from itertools import combinations

input = sys.stdin.readline

dwarf = [int(input()) for _ in range(9)]

height = list(combinations(dwarf, 7)) #일곱 난쟁이로 경우의 수 추리기

answer = []

for i in range(len(height)):
    if sum(height[i]) == 100: #문제 요구사항과 맞으면 저장
        answer = height[i]

answer = sorted(list(answer))

for i in range(len(answer)):
    print(answer[i])