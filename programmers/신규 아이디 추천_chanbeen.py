def solution(new_id):
    def level1(id):
        result = ''
        
        for i in id:
            result += i.lower()
        
        return result
    
    def level2(id):
        result = ''
        
        signs = ['-', '_', '.']
        
        for i in id:
            if 'a' <= i <= 'z': result += i
            if '0' <= i <= '9': result += i
            if i in signs: result += i
        
        return result
    
    def level3(id):
        result = ''
        
        flag = False

        for i in id:
            if i == '.':
                if flag == False:
                    result += i
                    flag = True
            else:
                result += i
                flag = False
        
        return result
    
    def level4(id):
        result = ''
        
        for i in range(len(id)):
            if i == 0 or i == len(id) - 1:
                if id[i] == '.':
                    continue
                    
            result += id[i]
            
        return result
    
    def level5(id):
        if len(id) == 0:
            return 'a'
        else:
            return id   
    
    def level6(id):
        if len(id) >= 16:
            id = level4(id[:15])
            
        return id
        
    def level7(id):
        if len(id) <= 2:
            while len(id) != 3:
                id += id[-1]
        
        return id
    
    answer = level1(new_id)
    answer = level2(answer)
    answer = level3(answer)
    answer = level4(answer)
    answer = level5(answer)
    answer = level6(answer)
    answer = level7(answer)
                
    return answer