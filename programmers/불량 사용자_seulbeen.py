#순열 사용까지는 ok
#순열로 각 경우의 수에 대한 집합을 ban_cases라는 리스트에 append하는 아이디어 구글링
from itertools import permutations
def need_ban(u_ids, banned_id):
    for i in range(len(banned_id)):

        if len(u_ids[i]) != len(banned_id[i]):
            return False

        for j in range(len(u_ids[i])):
            if banned_id[i][j] == "*":
                continue
            if u_ids[i][j] != banned_id[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = 0
    ban_cases = []
    cases = list(permutations(user_id, len(banned_id)))
    for each_case in cases:
        if not need_ban(each_case, banned_id):
            continue
        else:
            each_ban_case = set(each_case)
            if each_ban_case not in ban_cases:
                ban_cases.append(each_ban_case)

    return len(ban_cases)
