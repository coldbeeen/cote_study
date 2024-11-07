# DP겠지?
def solution(land):
    answer = 0
    row = len(land)
    
    for i in range(1, row):
        for j in range(4):
            prev = 0
            for k in range(4):
                #같은 열 제외
                if j != k:
                    #이전 행 값들 중 최댓값 저장
                    prev = land[i - 1][k] if prev < land[i - 1][k] else prev
            # 이전 행중 가장 큰 값(같은 열 제외) 더하기
            land[i][j] += prev

    #마지막 행의 가장 큰 값 반환
    answer = max(land[-1])
    return answer
