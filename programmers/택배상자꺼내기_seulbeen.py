# 1시간 46분
def solution(n, w, num):
    answer = 0
    # 그냥 위로 쭉 쌓는경우에는 n-num개 꺼내고, 꺼내려는 상자 꺼내고
    if w == 1:
        return n - num + 1

    # 몫과 나머지를 활용하기 위해 상자 번호를 -1 해줌
    num -= 1
    n -= 1
    # ex2)
    # 12
    # 11 10 9 8 7 6
    #  0  1 2 3 4 5

    row = num // w
    col = num % w

    # 짝수층은 정방향, 홀수층은 역방향
    # 홀수층이면
    if row % 2 == 1:
        col = w - col - 1

    top_row = n // w
    top_col = n % w
    # 일단 최고높이 박스 직전층까지 꺼내고,
    answer += top_row - row

    # 최고높이 박스가 홀수충이면 역방향
    if top_row % 2 == 1:
        top_col = w - top_col - 1
        # 위에 최고층 이 더있으면 하나 더뺌

        # 역방향 조건문
        if top_col <= col <= w:
            answer += 1

    else:
        # 정방향 조건문
        if 0 <= col <= top_col:
            answer += 1

    return answer
