n = int(input())

def is_valid(r_idx):
    # 현재 행: r_idx, 현재 열: row[r_ix] 을 이전 퀸들의 위치를 통해 놓을 수 있는지 검사
    for i in range(r_idx):
        if row[i] == row[r_idx] or abs(r_idx - i) == abs(row[r_idx] - row[i]):  # row[i]는 column index임. r_idx와 i가 row 값 담당. row의 각 요소는 column 값 담당
            return False
    return True

def backtrack(r_idx):
    global result
    if r_idx == n:  # 만약 현재 후보군이 유효한 해라면 result 1 증가 후 종료
        result += 1
        return

    for next_queen in range(n):  # 0 ~ 3열에 시도
        row[r_idx] = next_queen  # r_idx 행, next_queen 열에 퀸 배치
        if is_valid(r_idx):  # 유효한 위치라면
            backtrack(r_idx+1)  # 이어서 재귀

row = [0 for i in range(n)]  # index 0~3이 행을, row[0~3]이 열을 의미 (각 행에 있을 수 있는 퀸은 단 한개 => 1차원 리스트로 해결 가능)
result = 0
backtrack(0)  # 빈 체스판에서부터 시작
print(result)


# 하나 깨달은 게, 리스트같은 객체는 함수에서 global 안해줘도 접근이 가능한데, 그냥 정수값을 담은 변수는 접근이 안되네요