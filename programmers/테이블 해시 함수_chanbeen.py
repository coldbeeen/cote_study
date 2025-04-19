#약 24분 소요

def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key = lambda x : (x[col - 1], -x[0])) #1순위 : col번째 컬럼 오름차순, 2순위 : 기본키 컬럼 내림차순
    
    S_list = []
    
    for i in range(row_begin - 1, row_end):
        num = 0
        
        for j in range(len(sorted_data[i])):
            num += sorted_data[i][j] % (i + 1) #S_i 구하기
        
        S_list.append(num)
    
    answer = S_list[0]
    
    for i in range(1, len(S_list)):
        answer = answer ^ S_list[i] #XOR 연산
    
    return answer

#첫번째 컬럼은 기본키
#col번째 컬럼 값 기준 오름차순 정렬, col번째 컬럼 값 동일시 기본키 값 기준 내림차순 정렬
#a ^ b : a와 b XOR 연산
#참고) a | b : OR, a & b : AND, ~a : NOT