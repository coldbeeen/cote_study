# 31분
# 먼저 달팽이 배열에 채우고 나서 일차원으로 만들자
# 플래그로 진행방향 컨트롤하자
def solution(n):
    answer = []
    # 틀에 맞는 달팽이 배열
    snail = [[0] * i for i in range(1, n + 1)]

    # 0:(좌 아래) 1: (우) 2:(좌 위)
    flag = 0

    # 달팽이 배열의 원소 개수 겸 마지막 인덱스의 값
    len_snail = sum(i for i in range(1, n + 1))

    # 초기 설정
    i, j = 0, 0
    num = 1
    snail[0][0] = 1

    # 현재 상황에 맞는 플래그 변경해주는 함수
    def check():
        # 플래그의 변동 순서는 무조건 0->1->2->0... 순임

        # 좌 아래 플래그 일때
        if flag == 0:
            # 맽 아래까지 다 내려왔거나, 다음 위치가 이미 채워 진경우 (우)플래그로 변경
            if len(snail) - 1 == i or snail[i + 1][j] != 0:
                return 1

        # 우측 플래그 일때
        if flag == 1:
            # 맨 오른쪽까지 다 이동했거나, 다음 위치가 이미 채워 진경우 (좌 위)플래그로 변경
            if j == len(snail[i]) - 1 or snail[i][j + 1] != 0:
                return 2
        # 좌 위 플래그 일때
        if flag == 2:
            # 다음 위치가 이미 채워 진경우 (좌 아래)플래그로 변경(맨 위는 1이기 때문에 맨 위까지 올라가는 경우는 없음)
            if snail[i - 1][j - 1] != 0:
                return 0

        # 플래그 변동할 필요가 없는 경우 현재 플래그 유지
        return flag

    # 인덱스가 다 채워지는 동안
    while num < len_snail:
        # 플래그 변경함수
        flag = check()

        # 좌 아래 플래그인경우 다음 행으로
        if flag == 0:
            i += 1

        # 우 플래그인 경우 우측으로
        elif flag == 1:
            j += 1
        # 좌 위 플래그인 경우 좌측 위로
        else:
            i -= 1
            j -= 1

        # 플래그에 따른 인덱스 이동후 값 저장
        num += 1
        snail[i][j] = num

    # 달팽이 배열을 일차원 배열로 저장
    for s in snail:
        answer.extend(s)

    return answer
