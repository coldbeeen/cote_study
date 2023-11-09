import sys
from itertools import combinations
input = sys.stdin.readline

heights = [int(input()) for i in range(9)]
for comb in combinations(heights, 7):
    if sum(comb) == 100:
        break

for i in sorted(comb):
    print(i)