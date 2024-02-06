import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for i in range(n)]

for i in info:  # 모든 신체 정보 순회
    biggerCnt = 0
    for j in info:
        if i[0] < j[0] and i[1] < j[1]:  # 몸무게 키 둘 다 크면 카운트 증가
            biggerCnt += 1

    print(biggerCnt + 1, end=' ')  # 해당 카운트 + 1을 순위로 출력