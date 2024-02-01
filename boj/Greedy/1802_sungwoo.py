import sys
input = sys.stdin.readline

def check_and_split(foldStr):  # 접을 수 있다면 True를 반환하는 재귀함수: 맞은편 인덱스 검사 및 절반 분할 후 재호출 (분할된 문자열도 조건을 만족해야 함)
    if len(foldStr) == 1:  # 한 개까지 분할된 경우 True(참) 반환
        return True

    mid = len(foldStr) // 2  # 중앙 인덱스
    i = 0
    while i < mid:  # 맞은편 인덱스 값과 달라야 함 (out인 경우 맞은 편은 in)
        if foldStr[i] == foldStr[-(i+1)]:  # 같은 경우 접을 수 없음
            return False
        i += 1

    if check_and_split(foldStr[:mid]):
        return True

caseNum = int(input())

for _ in range(caseNum):
    foldStr = list(map(int, input().rstrip()))

    if check_and_split(foldStr):  # 재귀함수 호출
        print("YES")
    else:
        print("NO")