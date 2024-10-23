# 구글링

def convert_to_int(time):
    hour, minute, second = time.split(':')
    
    return int(hour) * 3600 + int(minute) * 60 + int(second) 

def convert_to_str(time):
    hour, minute, second = time // 3600, time % 3600 // 60, time % 60
    
    return f'{hour:02}:{minute:02}:{second:02}'

def solution(play_time, adv_time, logs):
    play_time = convert_to_int(play_time)
    adv_time = convert_to_int(adv_time)
    
    time_array = [0] * (play_time + 1)
    
    for log in logs:
        start, end = log.split('-')
        
        start = convert_to_int(start)
        end = convert_to_int(end)
        
        time_array[start] += 1
        time_array[end] -= 1 #시청 시작과 끝을 표시
        
    for i in range(1, len(time_array)):
        time_array[i] = time_array[i] + time_array[i - 1]
    # 매 초를 인덱스로 하여, 각 인덱스에서의 시청자 수를 기록
        
    for i in range(1, len(time_array)):
        time_array[i] = time_array[i] + time_array[i - 1]
    # 이전 코드를 반복하여, 이번에는 각 인덱스에서의 누적 시청자 수를 기록
    
    max_view = 0
    max_time = 0
    
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if max_view < time_array[i] - time_array[i - adv_time]: # 누적을 해놨으므로 광고 시작 전 값을 빼주면 광고 진행 동안의 시청자 수 계산 가능
                max_view = time_array[i] - time_array[i - adv_time]
                max_time = i - adv_time + 1 # 구간의 시작 시간
        else: #영상 시간과 광고 시간의 같을 때
            if max_view < time_array[i]:
                max_view = time_array[i]
                max_time = i - adv_time + 1
    
    return convert_to_str(max_time)

# 단순하게 for문과 sum함수를 같이 사용하면 시간 초과
# 아이디어가 생각이 나지 않아서 구글에서 찾아보니, '파괴되지 않은 건물'과 유사한 누적합 유형
# 같은 코드를 2번 사용해서 누적합을 구현하는 걸 보고 머릿속으로 벽을 느꼈음
