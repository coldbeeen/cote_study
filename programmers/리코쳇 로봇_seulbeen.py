# 대략 30분 추가하면되려나
def solution(board):
    answer = 0
    # 좌 우 상 하
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    row = len(board)
    col = len(board[0])
    visit=[[False for _ in range(len(board[0]))]for _ in range(len(board))]
    def dfs(cur_i, cur_j, flag, cnt):
        if board[cur_i][cur_j] == "D" or cur_i == row  or cur_j == col:
            return cnt + 1
        if board[cur_i][cur_j] == "R" and visit[cur_i][cur_j]:
            return -1

        for i in range(4):
            ci = cur_i + di[i]
            cj = cur_j + dj[i]
            if i == flag:

                dfs(ci, cj, i, cnt + 1)
            # if board[ci][cj]=="G":
            #     return cnt

    x, y = 0, 0
    flag=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                x = i
                y = j
                flag=1
                break
        if flag==1:
            break

    for i in range(4):
        # answer=max(dfs(0,0,i),answer)
        answer = max(dfs(x, y, i, 0), answer)
    return answer
l=[]
for _ in range(5):
    l.append(input())
output=solution(l)
print(output)