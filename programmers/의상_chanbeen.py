def solution(clothes):
    answer = 1
    
    cloth_dict = {}
    
    for i in range(len(clothes)):
        if clothes[i][1] not in cloth_dict.keys():
            cloth_dict[clothes[i][1]] = 2 #안 입는 것도 개수에 포함
        else:
            cloth_dict[clothes[i][1]] += 1
    
    for item, count in cloth_dict.items():
        answer *= count
    
    answer -= 1
                    
    return answer