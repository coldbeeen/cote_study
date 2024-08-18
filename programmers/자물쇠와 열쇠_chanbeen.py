#구글링

def rotate(key): #90도씩 회전
    M = len(key[0])
    
    new_key = [[0] * M for _ in range(M)]
    
    for i in range(M):
        for j in range(M):
            new_key[j][M - 1 - i] = key[i][j]
            
    return new_key

def check(new_lock): #확장된 자물쇠가 입력으로 들어오지만, 실제 자물쇠 범위만 탐색하면 됨
    lock_len = len(new_lock) // 3
    
    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    
    return True
            
def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    new_lock = [[0] * (N * 3) for _ in range(N * 3)] #배열 확장
    
    for i in range(N):
        for j in range(N):
            new_lock[i + N][j + N] = lock[i][j]
    
    for _ in range(4): #90도씩 4번 회전
        for i in range(N * 3 - M): #new_lock 배열을 key가 슬라이딩 윈도우로 순환, 그래서 인덱스 에러 방지를 위해 -M을 해줘야 함
            for j in range(N * 3 - M):
                for x in range(M):
                    for y in range(M):
                        new_lock[i + x][j + y] += key[x][y] #열쇠의 값들을 확장된 자물쇠에 덧셈
                        
                if check(new_lock) == True:
                    return True
                
                for x in range(M):
                    for y in range(M):
                        new_lock[i + x][j + y] -= key[x][y] #더해줬던 열쇠의 값들을 확장된 자물쇠에서 뺄셈
                        
        key = rotate(key) #열쇠 회전
    
    return False