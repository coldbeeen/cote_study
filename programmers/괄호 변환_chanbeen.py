#약 52분 소요

def solution(p):
    def split(p): #문자열 분리 함수
        u = ''
        v = ''
        
        cnt1 = 0
        cnt2 = 0
        
        for i in range(len(p)):
            if p[i] == '(':
                u += p[i]
                cnt1 += 1
            else:
                u += p[i]
                cnt2 += 1
            
            if cnt1 == cnt2: # (와 )의 개수가 같아질 때 u 만들기 중단, 나머지는 v로
                v = p[i + 1:]
                break
        
        return u, v
            
    
    def check(p): #올바른 괄호 문자열인지 확인하는 함수
        stack = []
        
        p = list(p)
        
        for i in range(len(p)):
            if p[i] == '(':
                stack.append(p[i])
            
            if p[i] == ')':
                
                if len(stack) == 0: #(이 없는데 )가 나온 것은 짝이 맞지 않음
                    return False
                
                stack.pop()
            
        if len(stack) == 0: #(과 )이 올바르게 구성되어 있음
            return True
        else:
            return False
    
    def function(p):
        if len(p) == 0: #빈 문자열 반환
            return ''
        
        if check(p): #처음부터 올바른 문자열이면 반환
            return p
        
        u, v = split(p)
        
        string = ''
        
        if check(u): #조건 3
            string += u
            string += function(v)
        else: #조건 4
            string += '('
            string += function(v)
            string += ')'
            
            for i in range(1, len(u) - 1): #
                if u[i] == '(':
                    string += ')'
                else:
                    string += '('
        
        return string
            
    answer = ''
    
    answer = function(p)
    
    return answer

#문자열 분리하는 함수 만들기
#올바른 괄호 문자열인지 체크하는 함수 만들기

#문제 조건대로 구현했더니 간단히 풀리는 문제