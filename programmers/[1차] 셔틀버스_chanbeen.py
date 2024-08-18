#구글링

def solution(n, t, m, timetable):
    answer = ''
    
    timetable = sorted([int(i[:2])*60+int(i[-2:]) for i in timetable], reverse=True) #분단위로 환산 + 역순 정렬
    
    bus_time = 9 * 60 #9시 정각
    
    for _ in range(n - 1): #마지막 버스 전까지
        for _ in range(m): #먼저 온 대기자들에서 탑승 가능 인원만큼 대기자 리스트에서 pop
            if len(timetable) > 0 and timetable[-1] <= bus_time:
                timetable.pop()
        
        bus_time += t #다음 버스 시간으로 이동
    
    con = bus_time if len(timetable) < m or timetable[-m] > bus_time else timetable[-m] - 1
    #남은 인원이 태울 수 있는 인원만큼 여유가 있거나, 다음 버스 시간보다 다음 대기자가 늦게 도착할 경우 버스가 도착하는 시간에 도착해도 탑승 가능
    #그렇지 않을 경우에는 원래 m번째 탑승하는 대기자보다 콘이 1분 일찍 도착해야 탈 수 있음
    con = f'{con//60:02d}:{con%60:02d}' #형태 변환
    
    answer = con
    
    return answer