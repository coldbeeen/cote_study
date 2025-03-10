# 15분
# 매번 슬라이스해서 토핑의 종류를 비교하려니 당연히 시간초과 떴음
# 철수와 동생의 토핑을 딕셔너리로 관리
# 철수가 나눠주는게 아니라 동생이 나눠주는거라고 가정하고, 모든 토핑을 초기에 동생이 보유
# 하나씩 철수가 동생의 토핑을 뺏어온다는 느낌으로 딕셔너리 갱신 후 비교
from collections import defaultdict


def solution(topping):
    answer = 0
    p1 = defaultdict(int)
    p2 = defaultdict(int)

    # 동생이 모든 토핑 차지
    for t in topping:
        p2[t] += 1
    # 철수가 하나씩 토핑을 뺏음
    for t in topping:
        p1[t] += 1
        p2[t] -= 1

        if p2[t] == 0:
            del p2[t]
        # 보유하고있는 토핑의 종류가 같으면 answer+=1
        if len(p1) == len(p2):
            answer += 1
    return answer


# from collections import Counter as counter
# def solution(topping):
#     answer = 0
#     for i in range(1,len(topping)):
#         p1=counter(topping[:i])
#         p2=counter(topping[i:])
#         if len(p1)==len(p2):
#             answer+=1
#     return answer
