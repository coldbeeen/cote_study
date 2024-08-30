def solution(m, n, board):

    answer = 0

    # board의 행을 'str'에서 'list'로 변환
    for i in range(m):
        board[i] = list(board[i])

    # 더 이상 사라지는 블록이 없을 때 까지
    while True:
        to_remove = set()  # 사라지는 블록의 좌표를 담는 set

        # 모든 좌표를 순회하며
        for i in range(m-1):
            for j in range(n-1):
                # 2x2 블록이 모두 같은 모양일 때 to_remove에 추가함
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] and board[i][j] is not None:
                    for xy in [(i,j), (i, j+1), (i+1, j), (i+1, j+1)]:
                        to_remove.add(xy)

        # 사라지는 블록이 없다면 반복문 종료
        if len(to_remove) == 0:
            break

        # to_removed를 통해 지울 블록을 계산하고 해당 위치의 블록을 지움 (to None)
        answer += len(to_remove)
        for i, j in to_remove:
            board[i][j] = None

        # 열 별로 빈 공간을 채워줌
        for j in range(n):
            not_none_block = []

            for i in range(m):  # None이 아닌 블록을 담음
                if board[i][j] is not None:
                    not_none_block.append(board[i][j])

            for i in range(m):  # None이 아닌 블록을 그대로 채워넣음 (빈 블록은 None으로)
                if i < m-len(not_none_block):
                    board[i][j] = None
                else:
                    board[i][j] = not_none_block[i - (m-len(not_none_block))]

    return answer  # 총 지워진 블록 리턴


print(
    solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	)
)