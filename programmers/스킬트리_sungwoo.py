def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:  # 스킬트리 순회

        skill_tmp = ""  # 선행스킬(skill)인 스킬을 담기 위한 빈 문자열

        for s in skill_tree:  # 각 스킬을 순회하며 선행스킬을 담음
            if s in skill:
                skill_tmp += s

        if skill_tmp == skill[:len(skill_tmp)]:  # 담은 스킬이 선행스킬 순서와 일치하는지 확인
            answer += 1

    return answer