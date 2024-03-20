import sys

input= sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

total = 0
result = -float("inf")
for i in range(n):
    total += array[i] # 연속합 계산

    if total > result:
        # 연속합이 기존의 연속합 최대보다 클 경우 갱신
        result = total
    if total < 0:
        # 연속합이 음수가 되는 순간, 뒤를 더해도 최대보다 커질 수 없음. 다시 시작
        total = 0

print(result)