def solution(survey, choices):
    answer = ''
    
    types = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        char1, char2 = survey[i][0], survey[i][1]
        
        if choices[i] < 4: 
            types[char1] += 4 - choices[i]
        else:
            types[char2] += choices[i] - 4
    
    types_list = list(types.items())
    
    for i in range(0, len(types_list), 2):
        if types_list[i][1] < types_list[i + 1][1]:
            answer += types_list[i + 1][0]
        else:
            answer += types_list[i][0]
        
    return answer