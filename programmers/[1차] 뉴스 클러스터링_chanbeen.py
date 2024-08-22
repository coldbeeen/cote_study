def solution(str1, str2):
    answer = 0
    
    str1_list = []
    str2_list = []
    
    intersect = []
    union = []
    
    str1, str2 = str1.upper(), str2.upper()
    
    for i in range(len(str1) - 1):
        tmp = str1[i:i+2]
        
        if 'A' <= tmp[0] <= 'Z' and 'A' <= tmp[1] <= 'Z':
            str1_list.append(tmp)
            
    for i in range(len(str2) - 1):
        tmp = str2[i:i+2]
        
        if 'A' <= tmp[0] <= 'Z' and 'A' <= tmp[1] <= 'Z':
            str2_list.append(tmp)
    
    while len(str1_list) != 0 and len(str2_list) != 0:
        elem = str1_list.pop()
        
        if elem in str2_list:
            intersect.append(elem)
            str2_list.remove(elem)
        
        union.append(elem)
    
    while len(str1_list) != 0:
        elem = str1_list.pop()
        
        union.append(elem)
        
    while len(str2_list) != 0:
        elem = str2_list.pop()
        
        union.append(elem)
    
    answer = 65536 if len(intersect) == 0 and len(union) == 0 else int((len(intersect)/len(union) * 65536))
    
    return answer