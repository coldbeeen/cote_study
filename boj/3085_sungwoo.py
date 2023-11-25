import sys
from copy import deepcopy
input = sys.stdin.readline


def sum_of_continuous_same_color(x):  # 행 또는 열을 받아 연속된 같은 색의 사탕의 가장 높은 개수 출력
    max_cnt = 0
    prev, tmp_sum = x[0], 1

    for i in x[1:]:
        if i == prev:
            tmp_sum += 1
        else:
            max_cnt = max(max_cnt, tmp_sum)
            tmp_sum = 1
        prev = i
    max_cnt = max(max_cnt, tmp_sum)
    return max_cnt

n = int(input())
board = [list(input().rstrip()) for i in range(n)]

result = 0

for i in range(n):  # 각 행의 열과 열 사이의 사탕 교환 시도
    for j in range(n-1):
        if board[i][j] != board[i][j+1]:  # 인접 사탕이 다르면 교환 시도
            new_board = deepcopy(board)
            new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]  # 스왑
            sum_list = []
            for idx in range(n):  # 모든 행 검사
                row = list(new_board[idx][k] for k in range(n))
                sum_list.append(sum_of_continuous_same_color(row))
            for idx in range(n):  # 모든 열 검사
                col = list(new_board[k][idx] for k in range(n))
                sum_list.append(sum_of_continuous_same_color(col))
            result = max(result, max(sum_list))  # 최댓값 갱신
for i in range(n-1):  # 각 열의 행과 행 사이의 사탕 교환 시도
    for j in range(n):
        if board[i][j] != board[i+1][j]:  # 인접 사탕이 다르면 교환 시도
            new_board = deepcopy(board)
            new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]  # 스왑
            sum_list = []
            for idx in range(n):  # 모든 행 검사
                row = list(new_board[idx][k] for k in range(n))
                sum_list.append(sum_of_continuous_same_color(row))
            for idx in range(n):  # 모든 열 검사
                col = list(new_board[k][idx] for k in range(n))
                sum_list.append(sum_of_continuous_same_color(col))
            result = max(result, max(sum_list))  # 최댓값 갱신

print(result)