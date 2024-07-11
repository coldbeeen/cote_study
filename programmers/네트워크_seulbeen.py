def solution(n, computers):
    answer = 0
    global visit
    visit = [False for _ in range(n)]

    for i in range(n):
        if visit[i] == False:
            DFS(n, computers, i)
            answer += 1

    return answer


def DFS(n, computers, idx):
    visit[idx] = True
    for i in range(n):
        if i != idx and computers[idx][i] == 1 and visit[i] == False:
            DFS(n, computers, i)
