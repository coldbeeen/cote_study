import sys
input = sys.stdin.readline

n = int(input())
requests = sorted(list(map(int, input().split())), reverse=True)
total = int(input())

result = requests[0]  # max request, 상한액

while result >= 0:  # 상한액을 줄여가며 조건에 맞는 상한액을 탐색

    tmpTotal, i = total, 0
    while i < n:  # 정렬된 리스트를 순회하며
        tmpTotal -= (requests[i] if requests[i] <= result else result)  # 임시 총액에서 상한액에 따른 예산을 차감
        if tmpTotal < 0:  # 만약 임시 총액이 음수가 된다면 상한액을 더 줄여야 하는 것이므로 break
            break
        i += 1
    else:  # braek에 걸리지 않았다면 조건을 만족하는 상한액이므로 출력 후 break
        print(result)
        break
    result -= 1