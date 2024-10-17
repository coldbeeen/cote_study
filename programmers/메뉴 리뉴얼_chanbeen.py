from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        cnt = {}
        comb = []
        
        for o in orders:
            o = sorted(o) #사전 순 정렬
            comb.extend(list(combinations(o, c))) #등장한 메뉴 조합에서, 코스 개수만큼 가능한 경우의 수 조합
            
        for case in comb:
            order = ''.join(case) #문자열로 변환
            
            if order in cnt:
                cnt[order] += 1
            else:
                cnt[order] = 1 #딕셔너리 value 계산
                
        for count in cnt:
            if cnt[count] == max(cnt.values()): #가장 많이 선호
                if cnt[count] > 1: #2명 이상
                    answer.append(count)
    
    return sorted(answer) #사전 순 정렬