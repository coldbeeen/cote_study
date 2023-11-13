import sys
input = sys.stdin.readline

def x이하의_삼각수(x):  # x이하의 삼각수를 리스트로 반환
    i = 1
    삼각수s = []
    while True:
        삼각수 = (i * (i+1)) / 2
        if 삼각수 > x:
            break
        삼각수s.append(삼각수)
        i += 1

    return 삼각수s

numOfLine = int(input())

for i in range(numOfLine):
    n = int(input())
    listOf삼각수 = x이하의_삼각수(n)  # 가능한 x 이하의 삼각수를 얻어

    flag = 0
    result = 0
    for i in listOf삼각수:  # 가능한 조합(순열)을 탐색
        for j in listOf삼각수:
            for k in listOf삼각수:
                if i + j + k == n:  # n이 만들어진다면 result 1,반복문 탈출
                    result, flag = 1, 1
                    break
            if flag: break
        if flag: break

    print(result)