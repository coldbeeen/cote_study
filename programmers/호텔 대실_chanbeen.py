#약 65분 소요

def convert_to_int(time):
    hour, minute = time.split(":")
    
    return int(hour)*60 + int(minute)

def solution(book_time):
    answer = 0
    
    for i in range(len(book_time)):
        for j in range(len(book_time[0])):
            book_time[i][j] = convert_to_int(book_time[i][j])
    
    time_sorted = sorted(book_time)
    
    end_time = []
    
    for i in range(len(time_sorted)):
        if len(end_time) == 0:
            end_time.append(time_sorted[i][1])
            answer += 1
            continue
        
        flag = 0
        
        for j in range(len(end_time)):
            if end_time[j] + 10 <= time_sorted[i][0]:
                end_time[j] = time_sorted[i][1]
                flag = 1
                break
        
        if flag == 0:
            end_time.append(time_sorted[i][1])
            answer += 1
    
    return answer

#29번째 줄에서 end_time[j]를 갱신해주지 않아서 15.8점이 계속 나왔었음
#생각해보면 end_time의 인덱스는 각 호실을 의미하는데, 그 호실에서 가장 최근 퇴실 시간으로 갱신해주지 않는 게 말이 안 됐음
#이거 찾느라 시간이 많이 소요됨