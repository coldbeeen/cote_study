import sys
input = sys.stdin.readline

n = int(input())
requests = sorted(list(map(int, input().split())))
total = int(input())


start, end = 0, requests[-1]
prev = 0

while start <= end:
    mid = (start + end) // 2
    limit = mid

    tmpTotal, i = total, n - 1
    while i >= 0:  # 정렬된 리스트를 순회하며
        tmpTotal -= (requests[i] if requests[i] <= limit else limit)  # 임시 총액에서 상한액에 따른 예산을 차감
        if tmpTotal < 0:  # 만약 임시 총액이 음수가 된다면 상한액을 더 줄여야 하는 것이므로 break
            end = mid - 1
            break
        i -= 1
    else:  # braek에 걸리지 않았다면 조건을 만족하는 상한액이나 최댓값을 찾아야하기 때문에 더 높은 상한액 탐색을 위해 범위를 위쪽으로 좁힘
        prev = limit  # 해당 값이 최댓값이었을 수 있기 때문에 prev에 저정함
        start = mid + 1

print(prev)  # 사전에 저장해둔 최댓값 출력