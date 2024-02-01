import sys
input = sys.stdin.readline

rope = []
result = []
n = int(input())

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)

for i in range(n):
    result.append((i+1) * rope[i])

print(max(result))