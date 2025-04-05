#9:45, 10:01 종료

import math

def solution(a, cylinder):
    answer = [0, 0]
    
    numer = 0 #분자
    denomi = 0 #분모
    
    for i in range(len(cylinder)):
        if cylinder[i]:
            continue
        else:
            idx = (i + 1) % len(cylinder) #발사x 확인 후, 다음 실린더
            flag = True
            
            for j in range(a):
                if cylinder[(idx + j) % len(cylinder)]:
                    flag = False
            
            if flag: #총알 발사 안 되는 케이스
                numer += 1
            
            denomi += 1
    
    if not numer: #만족하는 케이스 없음, 확률 0
        return [numer, 1]
    else:
        gcd = math.gcd(numer, denomi)
        
        if gcd != 1: #기약분수
            numer //= gcd
            denomi //= gcd
        
        return [numer, denomi]
    
    return answer

#위에 케이스 2개는 무시할 것
#방아쇠를 1번 당겼을 때 총알이 발사되지 않았으므로, 값이 1인 실린더는 분모로도 카운트하면 안 됨