# 딕셔너리로 참조해야 하고, 투 포인터를 원래 양끝값으로 했었는데 0,0으로 해야하는듯
from collections import defaultdict
def solution(gems):
    answer = [0, len(gems) - 1]
    gem_len = len(set(gems))
    left, right = 0, 0
    dic = defaultdict(int)
    dic[gems[0]] = 1
    while left <= right and right < len(gems):
        if len(dic) < gem_len:  # 모든 종류의 보석이 없다는 뜻
            right += 1
            if right >= len(gems):
                break
            dic[gems[right]] += 1

        else:  # 모든 종류의 보석은 있으니 최소길이로
            if right - left < answer[1] - answer[0]:
                answer[1] = right
                answer[0] = left
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                dic.pop(gems[left])
            left += 1

    answer[1] += 1
    answer[0] += 1
    return answer


# 이러면 시간초과 + 몇개 못맞춤
# def solution(gems):
#     answer = []
#     left = 0
#     right = len(gems) - 1
#     while left <= right:
#         if gems[right] in gems[left:right]:
#             right -= 1
#             continue
#         if gems[left] in gems[left + 1 : right + 1]:
#             left += 1
#             continue
#         if (
#             gems[right] not in gems[left:right]
#             and gems[left] not in gems[left + 1 : right + 1]
#         ):
#             # print(f"left : {left+1} right: {right+1}")
#             answer.append(left + 1)
#             answer.append(right + 1)
#             break
#     return answer
