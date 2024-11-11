from math import ceil

def solution(fees, records):
    answer = []
    
    default_time, default_fee, unit_time, unit_fee = fees
    
    parking = {}
    using_time = {}
    
    for record in records:
        time, number, io = record.split()
        hour, minute = map(int, time.split(":"))
        time = hour * 60 + minute
        
        if io == "IN":
            parking[number] = time
        elif io == "OUT":
            if number in using_time:
                using_time[number] += (time - parking[number])
            else:
                using_time[number] = time - parking[number] #머문 시간 계산
                
            del parking[number] #키 삭제
            
    for number, time in parking.items(): #OUT이 없는 차량들
        if number in using_time:
            using_time[number] += 1439 - time #1439는 23시간 59분
        else:
            using_time[number] = 1439 - time
            
    for number, time in sorted(using_time.items(), key = lambda x : x[0]): #차량 번호 순으로 정렬
        answer.append(default_fee + max(0, ceil((time - default_time) / unit_time)) * unit_fee) #예시에 적혀있는대로 주차 요금 계산
        
    return answer