import sys
input = sys.stdin.readline

cityNum = int(input())
road = list(map(int, input().split()))
gasPrice = list(map(int, input().split()))

# 시작 가격과 시작 비용 설정
minPrice = gasPrice[0]
result = minPrice * road[0]

for i in range(1, len(gasPrice)-1):  # 1부터 마지막 인덱스 직전까지 순회
    if gasPrice[i] < minPrice:  # minPrice 갱신 조건
        minPrice = gasPrice[i]

    result += minPrice * road[i]  # 비용 누적

print(result)