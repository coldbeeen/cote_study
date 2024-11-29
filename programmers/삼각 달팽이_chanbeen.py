#60분 +@, 구글링

def solution(n):
    answer = []
    
    snail = [[0] * n for _ in range(n)]
    
    num = 1
    x, y = -1, 0 #처음에는 아래로 진행
    
    for i in range(n):
        for j in range(i, n):
            
            if i % 3 == 0: #아래
                x += 1
            
            elif i % 3 == 1: #오른쪽
                y += 1
            
            elif i % 3 == 2: #위
                x -= 1
                y -= 1
            
            snail[x][y] = num #i, j가 아닌 별도의 x, y로 인덱스를 관리
            num += 1
    
    for i in range(n):
        for j in range(i + 1):
            answer.append(snail[i][j])
    
    return answer

#처음에는 c언어 시절 달팽이 문제처럼 direction 변수를 사용하려고 했으나 뜻대로 풀리질 않았음
#빈 2차원 배열을 선언하고 중간에 insert를 하는 부분에서 안 풀림

#첨부터 직각삼각형으로 생각하고, 인덱스 적으로 접근했다면 훨씬 쉬웠을 듯
#길이가 다른 직선을 방향 관리 해주면서 n번 그리니 삼각형이 완성되어 신기했던 문제 