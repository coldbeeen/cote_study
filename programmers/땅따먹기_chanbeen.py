def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            ex_list = land[i - 1].copy() #copy 안 하면 land의 요소도 같이 pop됨
            ex_list.pop(j)
            
            land[i][j] += max(ex_list)
    
    return max(land[len(land) - 1])