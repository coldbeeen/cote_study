import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

result = 0

for i in range(n-1):  # 합치는 횟수는 n-1. 카드가 하나뿐인 경우(앞뒤에 카드 없는 경우)는 실행 X -> 아래 조건문 OK)

    maxVal = max(l)
    maxIdx = l.index(maxVal)  # 최댓값 인덱스를 구함

    if maxIdx == 0:  # 앞에 카드가 없다면 뒤 카드와 합치기
        combineIdx = maxIdx+1
    elif maxIdx == n-1:  # 뒤에 카드가 없다면 앞 카드와 합치기
        combineIdx = maxIdx-1

    result += l[maxIdx] + l[combineIdx]  # 골드 누적
    del l[combineIdx]  # 합친 카드 소모

print(result)