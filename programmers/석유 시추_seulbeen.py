# DFS일듯
import sys
sys.setrecursionlimit(10**6)

def solution(land):
    answer = 0
    cnt = 0
    visit = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    #시간초과나서 찾아보니 이미 탐지한 석유를 저장해야 한다고 함
    oil = [0]

    def DFS(x, y, store):
        nonlocal cnt
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        #종료조건
        if x < 0 or x >= len(land) or y < 0 or y >= len(land[0]):
            return
        
        if land[x][y] == 1 and visit[x][y] == 0:
            #석유를 저장하기 위해서 visit배열에 석유덩어리 번호를 부여해주기 위함
            visit[x][y] = store

            cnt += 1
            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]
                DFS(cx, cy, store)

    for j in range(len(land[0])):
        total = 0
        check = []
        for i in range(len(land)):
            cnt = 0
            
            if land[i][j] == 1 and visit[i][j] == 0:
                #석유 덩어리 번호를 len(oil)로 (1번, 2번, 3번 ....)
                DFS(i, j, len(oil))
                # print("DFS완*******")
                # 한덩어리 탐색이 끝나면 total에 덩어리 크기 더해줌
                total += cnt
                #oil 값에 그 덩어리의 크기를 append -> [0,8] : 1번 덩어리에 8  
                oil.append(cnt)
                #check 배열에는 이미 계산에 포함되어있는 덩어리의 번호를 저장 (중복 방지)
                check.append(visit[i][j])
            
            # 석유칸인데 이미 방문한 칸일 경우
            elif land[i][j] == 1 and visit[i][j] != 0:
                # 계산에 포함되어있지 않았을때 저장했던 석유값 더해줌
                # 방문한 칸이고, 아까 계산에 포함한 덩어리이면 pass
                if visit[i][j] not in check:
                    total += oil[visit[i][j]]
                    check.append(visit[i][j])

                    # print(i,j)
                    # print(oil)
                    # print(total)
                    # print("##"*10)
        # 최대값 갱신
        if total > answer:
            answer = total

    return answer
