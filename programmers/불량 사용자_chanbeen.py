from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    
    def check(user, banned):
        for i in range(len(user)):
            if len(user[i]) != len(banned[i]): # 길이 하나라도 다르면 후보에서 제외
                return False
            
            for j in range(len(user[i])):
                if banned[i][j] == '*': # *일때는 검사 x
                    continue
                
                if user[i][j] != banned[i][j]:
                    return False
            
        return True
            
    candidates = list(permutations(user_id, len(banned_id)))
    results = []
    
    for candi in candidates:
        if check(candi, banned_id):
            candi = set(candi) #중복제거
            
            if candi not in results:
                results.append(candi)

    answer = len(results)   
        
    return answer