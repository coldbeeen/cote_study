def solution(skill, skill_trees):
    answer = 0
    
    skill = list(skill)
    
    for tree in skill_trees:
        tree = list(tree)
        
        idx = 0
        flag = 1
        
        for t in tree:
            if t in skill: #비효율적이라고 생각되는 부분
                if t == skill[idx]:
                    idx += 1
                else:
                    flag = 0
                    break
            
        if flag == 1: answer += 1
        
    return answer

# in 문법때문에 사실상 3중 반복문을 사용하는 꼴인데, 반복문 2개로 해결할 수 없었을까?