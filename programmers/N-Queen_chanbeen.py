#약 51분 소요

def solution(n):
    def check(x): #퀸 배치가 가능한지 체크
        for i in range(x): #퀸의 설치 가능 조건 : 가로, 세로, 대각선에 다른 퀸이 있으면 안 된다
            if row[x] == row[i]: #이미 해당 열 어딘가에 퀸이 있음
                return False
            
            if abs(row[x] - row[i]) == (x - i): #대각선은 (행 인덱스 간 차이) = (열 인덱스 간 차이)
                return False
        
        return True
        
    def n_queen(x):
        nonlocal answer #부모함수인 solution의 answer값 참조
        
        if x == n:
            answer += 1
            return
        else:
            for i in range(n): #설치 가능한 열이 있는지 확인
                row[x] = i #array[x][i]에 퀸 배치
                
                if check(x):
                    n_queen(x + 1)
        
    answer = 0
    
    row = [0] * n
    
    n_queen(0)
    
    return answer

#작년에 풀 때 1차원 배열로 압축해서 풀었던 것 같은데
#배열의 각 인덱스 : 행, 인덱스의 값 : 열
#Ex) array[0] = 1 : 0행 1열에 퀸을 배치하겠다
#대각선 체크하는 조건문 생각하는 데 오래 걸렸음

#마지막 테스트 케이스에서 시간 초과 발생
#주석 지워서 다시 제출하니까 통과되네?
#마지막 케이스 실행시간 보니 억까인 듯