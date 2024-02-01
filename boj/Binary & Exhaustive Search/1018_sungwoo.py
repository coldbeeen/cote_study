n, m = map(int, input().split())
board = [
    list(input()) for i in range(n)
]

dic = {'W': 1, 'B': -1}  # 딕셔너리 정의하여 'W'와 'B'를 *(-1) 연산으로 쉽게 스위칭할 수 있도록 함
result = []

for i in range(n - 7):  ## 체스판 시작 지점 설정 (행)
    for j in range(m - 7):  ## (열)

        cnt, flag = 0, 1  # 'W'로 시작하는 케이스
        for k in range(i, i + 8):  ## 체스판 8x8 범위 순회
            for l in range(j, j + 8):
                if dic[board[k][l]] != flag:  # 체스판 조건을 만족하지 않는다면 cnt 증가
                    cnt += 1
                flag *= -1
            flag *= -1
        result.append(cnt)  # cnt 추가

        cnt, flag = 0, -1  # 'B'로 시작하는 케이스
        for k in range(i, i + 8):  ## 체스판 8x8 범위 순회
            for l in range(j, j + 8):
                if dic[board[k][l]] != flag:  # 체스판 조건을 만족하지 않는다면 cnt 증가
                    cnt += 1
                flag *= -1
            flag *= -1
        result.append(cnt)  # cnt 추가

print(min(result))  # 최소 cnt 출력