# 이거 진짜 다 돌려서 찾는다고,,?
# 그래봤자 9C7 하면 36이긴 한데
import sys
input = sys.stdin.readline

from itertools import combinations

arr=[]

for _ in range(9):
    arr.append(int(input()))

combinations_of_7 = combinations(arr, 7)

for combo in combinations_of_7:
    if sum(combo) == 100:
        for num in sorted(combo):
            print(num)
        break   