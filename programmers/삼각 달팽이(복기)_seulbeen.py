# 28분


def solution(n):
    answer = []
    
    #삼각 달팽이 꼴에 맞는 배열 선언 및 초기화
    snail = [[0] * i for i in range(1, n + 1)]

    # 가장 마지막 번호
    len_snail = sum([i for i in range(1, n + 1)])
    
    # 방향 플래그 : left down, right,left up
    dir = "ld"
    i, j = 0, 0
    idx = 1

    #방향 플래그를 갱신하는 함수
    def dir_change():
        """방향의 전환은 항상 좌하향->우향->좌상향 순서임"""

        # 좌하향 플래그일때,
        if dir == "ld":
            # 최하단 도달 or 이미 값이 채워져있는 경우 right 플래그로 변환
            if i == n - 1 or snail[i + 1][j] != 0:
                return "r"
        # 우향 플래그일때,
        if dir == "r":
            # 최우측도달 or 다음 값이 이미 채워져 있는 경우 left up 플래그로 변환
            if j == n - 1 or snail[i][j + 1] != 0:
                return "lu"
        # 좌상향 플래그일때,
        if dir == "lu":
            # 이미 다음 값이 채워져있는 경우 좌하향 플래그 변환
            if snail[i - 1][j - 1] != 0:
                return "ld"
        # 플래그를 바꿀 필요 없는 경우 플래그 유지
        return dir

    snail[0][0] = 1
    while idx < len_snail:
        # 방향 플래그 변환
        dir = dir_change()

        #현재 플래그에 맞는 인덱스 갱신
        if dir == "ld":
            i += 1
        elif dir == "r":
            j += 1
        elif dir == "lu":
            i -= 1
            j -= 1

        # 인덱스에 값 갱신
        idx += 1
        snail[i][j] = idx
    # print(snail)

    #1차원 리스트로 펼쳐줌
    for s in snail:
        answer.extend(s)
    return answer


"""
일단 다 채우고 extend 하면 되지 않을까?
"""
