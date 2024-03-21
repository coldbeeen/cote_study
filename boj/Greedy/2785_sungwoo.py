import sys
input = sys.stdin.readline

chainNum = int(input())
chainList = sorted(list(map(int, input().split())))  # 정렬부터 해줘서 고리가 적은 체인이 맨 앞에 오도록

result = 0

while len(chainList) > 1:  # 체인이 하나만 남을 떄까지
    chainList[-1] += chainList.pop()  # 맨 앞 고리를 활용해 맨 뒤 두 체인을 묶어 주기

    if chainList[0] == 1:  # 맨 앞 체인의 고리가 1개였다면 그 고리과 위에서 묶은 체인 연결
        chainList[-1] += chainList.pop(0)  # 기존 1 삭제
    else:  # 위에서 맨 뒤 체인을 묶을 때 사용한 고리 빼주기
        chainList[0] -= 1
    result += 1

print(result)