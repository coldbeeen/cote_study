import sys

input = sys.stdin.readline

N = int(input())

budget = sorted(list(map(int, input().split())))

total = int(input())

result = 0

def sum_budget(mid):
    sum = 0
    
    for i in range(N):
        if budget[i] <= mid: #상한액 내
            sum += budget[i]
        else: #상한액 초과
            sum += mid
    
    return sum

left, right = 0, budget[-1]

if sum(budget) < total: #책정된 총 예산 내에서 해결할 수 있음
    result = budget[-1]
else:
    while left <= right:
        mid = (left + right) // 2 #mid : 특정한 정수 상한액
        if sum_budget(mid) > total:
            right = mid - 1
        else:
            left = mid + 1
            result = mid #제한 걸릴때는 mid가 배정된 예산 중 최댓값이 됨

print(result)
#총 시간 복잡도 : O(N log N)
#정렬 알고리즘도 O(N log N)이라고 함