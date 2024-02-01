import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

T = int(input())
num = [int(input()) for _ in range(T)]

gauss = []
n = 1
while n * (n + 1) // 2 <= 1000: #문제에서의 수 범위가 1000
    tri_num = n * (n + 1) // 2
    gauss.append(tri_num)
    n += 1

for i in range(len(num)):
    lower_tri_num = [x for x in gauss if x < num[i]] 
    #입력값보다 작은 삼각수로 추림
    cases = list(combinations_with_replacement(lower_tri_num, 3))
    #정확히 3개의 삼각수로 중복 허용해서 경우의 수 탐색
    for j in range(len(cases)):
        if sum(cases[j]) == num[i]:
            print(1)
            break
        
        if j == len(cases) - 1: #만족하는 경우의 수가 없음
            print(0)