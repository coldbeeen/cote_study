# 약 80분 소요

def solution(plans):
    answer = []
    
    for i in range(len(plans)): #시간 변환 및 자료형 변환 수행
        h, m = map(int, plans[i][1].split(':'))
        
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
        
    plans = sorted(plans, key = lambda x : x[1])
    
    stack = [] #잠시 멈춘 과제 저장용 스택
    
    for i in range(len(plans)):
        if i == len(plans) - 1: #다음이 없으므로 그냥 스택에 저장
            stack.append(plans[i])
            break
        
        name, start, t = plans[i]
        next_name, next_start, next_t = plans[i + 1]
        
        if start + t <= next_start: #다음 과제 시작 전 끝내기 가능
            answer.append(name)
            
            remain_time = next_start - (start + t) #잉여 시간
            
            while remain_time != 0 and stack: #멈춘 과제 있고 잉여 시간 있으면 멈춘 과제 수행
                r_name, r_start, r_t = stack.pop()
                
                if remain_time >= r_t:
                    answer.append(r_name) #잉여시간동안 과제 완료
                    remain_time -= r_t #잉여시간 갱신
                else: #잉여시간 동안 과제 완료 실패
                    r_t -= remain_time
                    stack.append([r_name, r_start, r_t])
                    remain_time = 0 #잉여 시간 소비 완료
                    
        else: #다음 과제 시작 시간과 겹치는 부분 O
            plans[i][2] = t - (next_start - start) #다음 과제 시작 전까지 해당 과제 수행
            
            stack.append(plans[i]) #과제를 잠시 멈춤
            
    while stack:
        answer.append(stack.pop()[0]) #남은 과제 순서대로 처리
                    
    return answer

#잠시 멈춘 과제 -> 스택 활용
#주어지는 시각은 변환
#다음 과제 시작 전에 과제 완료 가능/불가능 으로 케이스 나눠서 각각 구현
#잉여 시간을 나타내는 remain_time이라는 변수를 잘 관리해주는 것이 중요
#잉여 시간이 있고 stack에 과제가 있다면 pop해서 잉여 시간에 맞게 처리