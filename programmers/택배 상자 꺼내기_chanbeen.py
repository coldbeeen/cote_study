#약 21분 소요

def solution(n, w, num):
    answer = 0
    
    package = [[-1] * w for _ in range(n // w + 1)]
    
    row, col = 0, 0
    direction = 1
    
    for i in range(1, n + 1):
        package[row][col] = i
        
        if i % w == 0: #w개 놓았을 경우
            row += 1 #다음 열로 이동
            direction *= -1 #방향 전환
        else:
            col += direction #direction이 양수면 오른쪽, 음수면 왼쪽 진행
    
    for i in range(n // w + 1):
        for j in range(w):
            if package[i][j] == num: #원하는 택배 발견
                for k in range(i, n // w + 1):
                    if package[k][j] != -1:
                        answer += 1 #같은 열의 위에 위치한 택배 꺼내기
    
    return answer

#direction으로 방향을 조절하여 2차원 리스트 생성
#택배 박스가 없는 곳을 -1 값 저장
#원하는 택배 박스가 있는 열에서, 먼저 꺼내야 하는 박스만 for문으로 카운트
#무난히 통과