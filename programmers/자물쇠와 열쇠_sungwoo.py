from copy import deepcopy


def solution(key, lock):

    # key를 시계방향으로 90도 회전하는 함수
    def rotate():
        copied_key = deepcopy(key)  # 회전 로직 수행 시, 요소 값 손실을 피하기 위해 key 복사본을 만들어 수행
        for x in range(len(key)):
            for y in range(len(key)):
                key[x][y] = copied_key[len(key)-1-y][x]

    n, m = len(lock), len(key)
    hole_cnt = sum([row.count(0) for row in lock])  # 홈의 개수 (열쇠가 홈을 다 채우는지 판별하기 위함)

    # key가 lock을 벗어날 수 있기 때문에 lock을 3배의 크기로 확장하여 비교하도록 할 것임
    # (m - 1) + n + (m -1) 크기 정도로만 확장하면 되지만 편의를 위해서 3배로 함
    lock = [[1 for _ in range(n * 3)] for _ in range(n)] + \
          [[1 for _ in range(n)] + lock[i] + [1 for _ in range(n)] for i in range(n)] + \
          [[1 for _ in range(n * 3)] for _ in range(n)]

    # lock의 모든 위치를 순회하며 key를 넣어보도록 함 (각 순회마다 90도 회전 4번 수행)
    for i in range(n*3):
        for j in range(n*3):
            for _ in range(4):  # 회전을 위한 반복문 (4번 수행 시 원래대로 돌아옴)

                rotate()  # 회전 수행

                # flag는 자물쇠가 들어가는지, cnt는 홈에 들어간 돌기 횟수를 세기 위함
                flag, cnt = True, 0

                # key를 순회하며 비교 수행 (열쇠 삽입 수행)
                for key_i in range(m):
                    for key_j in range(m):
                        # lock의 가운데(center) 부분에 대해서만 비교를 수행
                        if n <= i + key_i < 2 * n and n <= j + key_j < 2 * n:
                            if key[key_i][key_j] == 1:  # 열쇠의 돌기 부분일 때,
                                if lock[i+key_i][j+key_j] == 1:  # 1. 자물쇠도 '돌기'라면 열쇠를 넣을 수 없음
                                    flag = False
                                else:  # 2. 자물쇠가 '홈'이라면 해당 돌기가 넣을 수 있음
                                    cnt += 1

                # 자물쇠에 열쇠를 넣을 수 있고, 모든 홈에 돌기가 끼워졌다면 자물쇠를 풀 수 있음
                if flag and cnt == hole_cnt:
                    return True

    return False

# lock이 아닌 key를 (이동으로 인한 돌기의 손실이 없도록) 3배 크기의 2차원 리스트로 만들어 회전 및 이동을 수행하며 lock과 비교하는 방식으로 수행했는데(63점),
# lock을 3배 크기의 3차원 리스트로 만든 뒤, key와 비교하는 방식이었습니다...