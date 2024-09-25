def solution(friends, gifts):
    #선물 개수 배열
    answer = [0 for _ in range(len(friends))]
    
    #주고받은 선물 표
    table = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    
    #선물 지수
    point = [0 for _ in range(len(friends))]

    # gifts 배열을 바탕으로 표 및 선물 지수 제작
    for case in gifts:
        case = case.split(" ")
        give = case[0]
        take = case[1]

        g_idx = friends.index(give)
        t_idx = friends.index(take)

        table[g_idx][t_idx] += 1
        point[g_idx] += 1
        point[t_idx] -= 1

    # 계산
    for i in range(len(friends)):
        # 한번에 자기 대칭 성분이랑 비교하므로 i+1 번째 부터 탐색하면 됨
        for j in range(i + 1, len(friends)):

            if table[i][j] > table[j][i]: # j에게 준 선물이 더 많은 경우
                answer[i] += 1

            elif table[i][j] < table[j][i]: # j에게 받은 선물이 더 많은 경우
                answer[j] += 1

            else: # 같은 경우 선물 지수 비교
                if point[i] > point[j]:
                    answer[i] += 1
                elif point[i] < point[j]:
                    answer[j] += 1
                else:
                    pass
    return max(answer)
