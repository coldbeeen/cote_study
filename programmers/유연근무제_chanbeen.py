#약 25분 소요

def solution(schedules, timelogs, startday):
    def convert_time(num):
        hour, minute = num // 100, num % 100
        
        return hour * 60 + minute
    
    answer = 0
    
    for i in range(len(schedules)):
        schedules[i] = convert_time(schedules[i]) #시간 변환
    
    for i in range(len(timelogs)):
        for j in range(len(timelogs[i])):
            timelogs[i][j] = convert_time(timelogs[i][j]) #시간 변환
        
    for i in range(len(schedules)):
        day = startday
        
        flag = True
        
        hope = schedules[i] #직원별 출근 희망 시각
        
        for j in range(len(timelogs[i])):
            if day == 6: #토요일
                day += 1
                continue
            
            if day == 7: #일요일 
                day = 1
                continue
                
            if hope + 10 < timelogs[i][j]: #지각
                flag = False
                break
                
            day += 1
        
        if flag:
            answer += 1
        
    return answer

#시간 계산 = 시 * 10 + 분
#토, 일은 출근하지 않으므로 배제해줘야함
#schedules : 출근 희망 시각, timelogs : 출근한 시각

#1차 제출
#1. %100으로 시 분을 나눈다음 60 * 시 + 분으로 schedules, timelogs 변환
#2. startday를 1씩 증가하면서, %7 했을 때 6이면 토요일, 0이면 일요일 => 패스
#3. startday가 7이 되면 1로 초기화
#무난하게 통과