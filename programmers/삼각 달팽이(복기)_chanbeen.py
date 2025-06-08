#약 36분 소요

def solution(n):
    answer = []
    
    array = [[0] * n for _ in range(n)]
    
    num = 1
    x, y = -1, 0 #첫 시작은 아래 방향이므로 x를 -1로 설정
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0: #아래
                x += 1
                
            elif i % 3 == 1: #오른쪽
                y += 1
                
            elif i % 3 == 2: #위
                x -= 1
                y -= 1
            
            array[x][y] = num
            num += 1
    
    for i in range(n):
        for j in range(i + 1):
            answer.append(array[i][j])
    
    return answer

#정사각형의 0으로 채워진 2차원 리스트를 생성한 뒤, 별도로 인덱스를 관리하며 값을 채워넣는 문제
#문제처럼 말고 직각삼각형으로 생각할 것
#2차원이므로 2중 반복문으로 해결
#방향 전환은 n번 일어나고, 방향은 아래 -> 오른쪽 -> 위 -> 아래 -> 오른쪽 -> ... 식으로 반복된다
#방향 전환의 종류 수가 3개이므로, 3으로 나눈 나머지로 방향을 관리
#방향 전환을 할 때마다 해당 방향으로 채우는 원소 개수는 1씩 감소, j의 범위를 i부터 n으로 설정하여 해결

#방향을 별도로 관리했던건 기억났으나 3의 나머지로 관리했던 걸 다시 떠올리는 게 힘들었던 문제