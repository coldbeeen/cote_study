import sys

input = sys.stdin.readline

N = int(input())

tip = sorted([int(input()) for i in range(N)], reverse=True) 
#팁 많이 주는 사람을 먼저 받아야 최대한 땡길 수 있음
result = 0
for i in range(N):
    result += tip[i] - i if tip[i] - i > 0 else 0

print(result)