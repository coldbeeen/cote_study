def solution(board, skill):

    n, m = len(board), len(board[0])
    answer = 0

    # acc[r][c]에 (0, 0) ~ (r, c)의 데미지의 합을 저장하기 위해 누적합 리스트 생성
    # (skill 순회에서 시간복잡도 O(n*m)이 걸리지 않게 하기 위함)
    acc = [[0 for _ in range(m)] for _ in range(n)]

    # skill 순회
    for t, r1, c1, r2, c2, degree in skill:

        damage = -degree if t == 1 else degree  # (type에 따른 데미지 설정)

        # (0, 0) ~ (r2, c2) 데미지 갱신
        acc[r2][c2] += damage

        # (r1, c1) ~ (r2, c2)가 아닌 위치에 적용된 데미지를 복구
        if r1 > 0:  # 윗 부분 복구
            acc[r1-1][c2] -= damage
        if c1 > 0:  # 왼쪽 부분 복구
            acc[r2][c1-1] -= damage
        if r1 > 0 and c1 > 0:  # 겹친 부분은 다시 더해줌
            acc[r1-1][c1-1] += damage

    # 누적합 리스트를 순회하며 원소별 데미지 계산 (1. 오른쪽에서 왼쪽으로, 2. 아래에서 위로)
    for i in range(n-1, -1, -1):
        for j in range(m-1, 0, -1):
            acc[i][j-1] += acc[i][j]
    for i in range(n-1, 0, -1):
        for j in range(m-1, -1, -1):
            acc[i-1][j] += acc[i][j]

    # 데미지를 받은 건물이 0보다 크다면 answer 1 증가
    for i in range(n):
        for j in range(m):
            if board[i][j] + acc[i][j] > 0:
                answer += 1

    return answer