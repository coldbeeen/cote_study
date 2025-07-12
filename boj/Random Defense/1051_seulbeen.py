# 숫자 정사각형
# 39분
# list index out of range가 발생했는데, 숫자를 받을때 공백이 없는지 모르고 split(" ")를 해줘서였음...

import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
# 사각형배열 선언 및 입력
rec = []
for _ in range(N):
    tmp = [int(n) for n in input().rstrip()]
    rec.append(tmp)


# print(rec)
def check(L):
    # 크기 L짜리의 정사각형의 각 꼭짓점을 체크 하는 함수
    for i in range(N - L + 1):
        for j in range(M - L + 1):
            if (
                rec[i][j]
                == rec[i + L - 1][j]
                == rec[i][j + L - 1]
                == rec[i + L - 1][j + L - 1]
            ):
                return True

    return False


# 정사각형 크기의 최댓값은 가로 세로중 작은 길이
upper_bound = min(N, M)

# 상한선부터 1까지, check 후 리턴
for i in range(upper_bound, 0, -1):
    if check(i):
        print(i**2)
        break
