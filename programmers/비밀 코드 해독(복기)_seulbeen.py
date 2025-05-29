# 9분
from itertools import combinations
def solution(n, q, ans):
    answer = 0

    # 1~n까지의 번호
    password = [i for i in range(1, n + 1)]

    def find_zero():

        # ans 중 값이 0인 index를 찾아서 리스트로 반환
        result = []
        for i in range(len(ans)):
            if ans[i] == 0:
                result.append(i)
        return result

    zeros = find_zero()
    # print(zeros)

    # ans가 0이라는 뜻 -> 아무것도 못맞췄다는 뜻 -> 그 번호은 비밀번호에 없다는 뜻 -> 지워도 됨
    for z in zeros:
        for nums in q[z]:
            try:
                password.remove(nums)
            except:
                pass
    # print(password)

    # 남아있는 후보들중 가능한 비밀번호들의 조합
    for c in combinations(password, 5):
        flag = True
        #q를 순회
        for i in range(len(q)):
            cnt = 0
            for j in range(5):
                # 각 번호가 비밀번호 후보에 있을때마다 cnt +1
                if q[i][j] in c:
                    cnt += 1
            # ans와 cnt 개수가 다르다면 탈락
            if cnt != ans[i]:
                flag = False
                break
        if flag:
            answer += 1
    return answer

"""
야구게임? 비스무리한 느낌
1. ans중 0, 즉 아무것도 못맞춘 경우를 먼저 찾아서, 해당 숫자를 경우의 수에서 싹 다 지움
2. 그 이후 각 q와 ans 별 조건에 맞는 경우를 찾음
"""