def solution(skill, skill_trees):
    answer = 0
    #스킬트리를 담을 리스트
    s_list = [i for i in skill]

    for each_skills in skill_trees:
        idx = 0 #첫 스킬이니 인덱스는 0
        flag = 1
        for s in each_skills:

            # 스킬트리를 지켜야 하는 스킬일 경우
            if s in skill:
                # 해당 스킬의 인덱스가 현재 가리키고 있는 인덱스와 다르면 불가능한 스킬트리
                if s_list.index(s) != idx:
                    flag = 0
                    break
                # 같다면 다음 스킬로 인덱스 이동
                else:
                    idx += 1
        if flag == 1:
            answer += 1
        else:
            flag = 1

    return answer
