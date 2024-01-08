# 이걸 백트래킹으로 어떻게 풀 수 있을꺼?

from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))
perms = permutations(arr, n)  # 순열 생성

result = 0

for perm in perms:  # 모든 순열 순회
    s = 0
    for i in range(n - 1):  # 식대로 계산
        s += abs(perm[i] - perm[i + 1])

    if s > result:  # 최댓값이라면 갱신
        result = s

print(result)