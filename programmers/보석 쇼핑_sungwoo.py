# 투 포인터 풀이 (l, r 모두 index: 0에서 시작)
def solution(gems):
    answer = []

    gems_set_len = len(set(gems))  # 고유한 보석의 개수

    # 투 포인터 탐색에 앞서, 딕셔너리를 활용해 보석의 개수를 관리할 것임 (그래야 cnt를 1로 유지하는 선에서 가장 짧은 구간을 구할 수 있음)
    gem_dict = {gems[0]: 1}
    l, r = 0, 0
    min_len = len(gems) + 1  # answer 업데이트 조건을 위한 min_len

    # 투 포인터 탐색 시작
    while l < len(gems) and r < len(gems):

        # gem_dict는 보석이 존재해야만 key가 존재함. 따라서 조건을 만족한다는 것은 모든 보석이 나왔다는 뜻임
        if len(gem_dict) == gems_set_len:

            # 구간의 길이가 min_len보다 짧다면 갱신!
            if r - l + 1 < min_len:
                min_len = r - l + 1
                answer = [l+1, r+1]

            # gems[l] 보석을 지우고 l += 1
            gem_dict[gems[l]] -= 1
            if gem_dict[gems[l]] == 0:
                del gem_dict[gems[l]]
            l += 1

        else:

            # r 포인터 탐색을 이어 나감
            r += 1

            # r이 인덱스 범위를 초과할 경우 즉시 종료!
            if r == len(gems):
                break

            # gems[r]의 보석을 추가 (있다면 개수 +1)
            gem_dict[gems[r]] = gem_dict.get(gems[r], 0) + 1

    return answer


print(solution(["AA", "AB", "AC", "AA", "AC"]))