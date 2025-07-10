#약 17분 소요

from collections import defaultdict

N, X = map(int, input().split())

visit = list(map(int, input().split()))

cases = defaultdict(int)

left = 0
right = X

cnt = 0
for i in range(right):
    cnt += visit[i]

cases[cnt] = 1

for i in range(N - X):
    cnt -= visit[left]
    cnt += visit[right]

    cases[cnt] += 1

    left += 1
    right += 1

cases = sorted(cases.items(), key = lambda x: x[0])

if not cases[-1][0]:
    print("SAD")
else:
    print(cases[-1][0])
    print(cases[-1][1])

#슬라이딩 윈도우 + 딕셔너리 + 정렬