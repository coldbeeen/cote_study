# 1826-1851
# 25분
# 중심으로부터 2,3,4
# 조합 완전탐색은 시간초과뜸
# 무게가 같으면 무조건 가능하니 1개추가
# 몸무게 비가 2:3, 2:4, 3:4, 3:2,4:2,4:3 인 경우에 짝꿍임
from itertools import permutations
from collections import defaultdict


def solution(weights):
    answer = 0
    # 시소 짝꿍 딕셔너리
    seesaw = defaultdict(int)
    # 미터 순열 경우의 수
    meter = list(permutations(range(2, 5), 2))

    for w in weights:
        # 몸무게가 같으면 추가
        answer += seesaw[w]

        for m in meter:
            # 비율에 대응되는 상대짝꿍 추가
            answer += seesaw[w * m[0] / m[1]]

        # 자기자신 +1 (첫 방문때는 답에 추가 안되지만 나중에 비율 맞는애가 있을때 걔한테 추가해주려고)
        seesaw[w] += 1

    return answer
