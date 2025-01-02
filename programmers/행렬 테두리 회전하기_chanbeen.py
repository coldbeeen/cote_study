def solution(rows, columns, queries):
    answer = []
    
    array = [[0 for col in range(columns)] for row in range(rows)]
    
    t = 1
    
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1
            
    for x1, y1, x2, y2 in queries:
        tmp = array[x1 - 1][y1 - 1] #한 칸 씩 옮기다 보면 사라지는 값 존재, 미리 저장
        min_num = tmp

        for i in range(x1 - 1, x2 - 1): #왼쪽 아래에서 위로
            move = array[i + 1][y1 - 1]
            array[i][y1 - 1] = move
            min_num = min(min_num, move)

        for i in range(y1 - 1, y2 - 1): #오른쪽 아래에서 왼쪽으로
            move = array[x2 - 1][i + 1]
            array[x2 - 1][i] = move
            min_num = min(min_num, move)

        for i in range(x2 - 1, x1 - 1, -1): #오른쪽 위에서 아래로
            move = array[i - 1][y2 - 1]
            array[i][y2 - 1] = move
            min_num = min(min_num, move)

        for i in range(y2 - 1, y1 - 1, -1): # 왼쪽 위에서 오른쪽으로
            move = array[x1 - 1][i - 1]
            array[x1 - 1][i] = move
            min_num = min(min_num, move)

        array[x1 - 1][y1] = tmp #미리 저장해놨던 값 옮기기
        
        answer.append(min_num) #문제 조건
    
    return answer