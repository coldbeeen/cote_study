import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
SG = sorted(list(map(int, input().split())))
M = int(input())
num = list(map(int, input().split()))

def count_by_range(list_, left, right): #이진탐색으로 개수 구하는 함수
    left_index = bisect_left(list_, left)
    right_index = bisect_right(list_, right)
    
    return right_index - left_index

for i in range(M):
    print(count_by_range(SG, num[i], num[i]), end=' ')