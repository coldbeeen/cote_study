# 재귀함수 + 백트래킹 구글링
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def subset_sum(idx, sub_sum):
    global cnt

    if idx >= n:
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1
    
    # 현재 arr[idx]를 선택한 경우의 가지
    subset_sum(idx+1, sub_sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    subset_sum(idx+1, sub_sum - arr[idx])

subset_sum(0, 0)
print(cnt)

# 브루트포스
'''
import sys
input = sys.stdin.readline

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)
'''