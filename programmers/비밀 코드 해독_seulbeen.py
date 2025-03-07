
from itertools import combinations


def solution(n, q, ans):
    answer = 0
    # 1-n 까지 숫자 배열
    nums = [i for i in range(1, n + 1)]

    # 0을 찾기 위함
    def rm_idx():
        result = []
        for i in range(len(ans)):
            if ans[i] == 0:
                result.append(i)
        return result

    rm = rm_idx()

    # 하나도 못맞춘 예측에 해당하는 숫자들을 지움
    for i in rm:
        for j in q[i]:
            try:
                nums.remove(j)
            except:
                pass

    for c in combinations(nums, 5):
        flag = 1
        for i in range(len(ans)):
            if ans[i] == 0:
                continue
            cnt = 0
            for j in q[i]:
                if j in c:
                    cnt += 1
            if cnt != ans[i]:
                flag = 0
                break
        if flag:
            answer += 1

    return answer
