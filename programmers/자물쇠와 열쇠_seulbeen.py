# 3번 회전가능
# 0,1 => 1,2, 0,2 =>2,2
# 1,0 => 0,1, 1,2=> 2,1
# 2,0 => 0,0 , 2,1 => 1,0
# 2x3 배열이라면?
# 1,2=> 2,0
# 회전 후의 행=회전 전의 열
# 회전시키기 전 행+ 회전 후 열 = 이전행 개수 -1


def rotate(key):
    len_key = len(key)
    deg90 = [[0] * len_key for _ in range(len_key)]

    for i in range(len_key):
        for j in range(len_key):
            deg90[i][j] = key[len_key - 1 - j][i]
    return deg90


def check(r, c, key, lock):
    cnt = 0
    for i in range(len(key)):

        for j in range(len(key)):

            if lock[r + i][c + j] == -1:  # 범위 밖이라서 열쇠의 돌기/홈 상관 없음
                continue
            
            elif lock[r + i][c + j] == 1: #자물쇠와 열쇠의 돌기가 맞닿으면 안됨
                if key[i][j] == 1:
                    return False
                
            else:  # == 0
                if key[i][j] == 0: #자물쇠의 홈과 열쇠의 홈으로는 열 수 없음
                    return False
                else: # 돌기와 홈이 만났을때 개수 +1
                    cnt += 1
    
    if cnt == zero_cnt: #자물쇠의 모든 홈을 채웠으면 열었다는 뜻
        return True
    
    return False


def solution(key, lock):
    answer = False

    global zero_cnt # 자물쇠의 홈 개수
    zero_cnt = 0

    for i in range(len(lock)): # 자물쇠의 홈 개수를 셈
        for j in range(len(lock)):
            if lock[i][j] == 0:
                zero_cnt += 1

    len_lock = len(lock)

    # 컨볼루션처럼, 자물쇠를 확장(실제 자물쇠가 가운데 위치하도록)
    extend_lock = [[-1] * (len_lock * 3) for _ in range(3 * len_lock)] 
    for i in range(len_lock):
        for j in range(len_lock):
            extend_lock[len_lock + i][len_lock + j] = lock[i][j]

    # 0도, 90도, 180도, 270도 총 4번의 반복문
    for _ in range(4):

        # #check
        for i in range(len(extend_lock) - len(key) - 1):  # -1 해도 되고 안해도 됨(어차피 다 -1인 부분을 탐색하는 케이스가 존재하기에 다 탐색할 필요가 없는 것)

            for j in range(len(extend_lock) - len(key) - 1):
                # 자물쇠를 열 수 있는지 check
                answer = check(i, j, key, extend_lock)

                if answer: #열 수 있으면 return
                    return answer
        # rotate
        key = rotate(key)

    return answer
