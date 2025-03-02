#약 24분 소요

import copy

def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i] #key : want, value : number
    
    for i in range(len(discount)):
        dict_copy = copy.deepcopy(want_dict) #딕셔너리 복사
        
        for j in range(10):
            if i + j >= len(discount):
                break
                
            key = discount[i + j]
            
            if key in dict_copy: #복사한 딕셔너리 내에서 value 차감
                dict_copy[key] -= 1
            
                if dict_copy[key] == 0: #want의 특정 물품에 대한 수량 만족 시 key 삭제
                    del dict_copy[key]
        
        if len(dict_copy.items()) == 0: #want 내 물품을 모두 만족했으면 그 날짜에 회원가입 가능
            answer += 1
            
    return answer

#매일 한 가지 제품 할인, 하루에 1개만 구매 가능
#원하는 제품을 모두 할인받을 수 있는 날짜의 개수를 return
#discount 길이 최대가 10만, 2중 반복문 사용가능할 듯
#want와 number는 각각 key와 value로 묶어서 딕셔너리로 관리
#want와 number의 길이가 10이하인 점에 유의하면서 코드 작성 결과, 무난히 통과 (최악 809.11ms)