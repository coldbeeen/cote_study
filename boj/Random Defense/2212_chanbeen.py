#구글링

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

pos = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
    sys.exit()

dist = []
for i in range(1, n):
    dist.append(pos[i] - pos[i-1]) #지점 간 거리

dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0) #가장 거리가 큰 지점은 집중국을 따로 두면 됨

print(sum(dist))