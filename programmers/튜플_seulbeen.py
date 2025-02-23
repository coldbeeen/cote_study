# 10분

import ast
def solution(s):
    answer = []
    cand = set()
    # {}를 []로 바꾼 후 리스트로 만듦
    s = s.replace("{", "[")
    s = s.replace("}", "]")
    s = ast.literal_eval(s)

    # 내부 리스트의 길이순으로 정렬
    s.sort(key=lambda x: len(x))
    cand.add(s[0][0])
    answer.append(s[0][0])

    for i in range(1, len(s)):
        # cand에 없는 원소일때 cand에 추가, answer에 추가 후 break
        for j in s[i]:
            if j not in cand:
                cand.add(j)
                answer.append(j)
                break

    return answer
