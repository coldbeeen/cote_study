# 6분
from collections import defaultdict


def solution(k, tangerine):
    answer = 0

    # 귤 크기별로 개수 딕셔너리에 저장
    gyul = defaultdict(int)
    for t in tangerine:
        gyul[t] += 1
    # 개수가 많은 순서대로 정렬
    gyul = sorted(gyul.items(), key=lambda x: x[1], reverse=True)

    for g in gyul:
        # k개 보다 귤 개수가 적다면 싹 다 선별
        if k > g[1]:
            k -= g[1]
            answer += 1
        # k개 보다 적거나 같으면 나머지 k개 선별 후 종료
        else:
            answer += 1
            break

    return answer
