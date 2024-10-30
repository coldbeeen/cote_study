def convert_str_to_int(time):
    time = time.split(':')
    
    return int(time[0]) * 60 + int(time[1])

def convert_int_to_str(time):
    minute, second = time // 60, time % 60
    
    return f'{minute:02}:{second:02}'

def solution(video_len, pos, op_start, op_end, commands):
    def check(time):
    
        return op_end if op_start <= time <= op_end else time
    
    answer = ''
    
    video_len = convert_str_to_int(video_len)
    pos = convert_str_to_int(pos)
    op_start= convert_str_to_int(op_start)
    op_end = convert_str_to_int(op_end)
    
    pos = check(pos)
    
    for c in commands:
        if c == 'prev':
            pos = pos - 10 if pos > 10 else 0
        elif c == 'next':
            pos = pos + 10 if pos + 10 < video_len else video_len
            
        pos = check(pos)
    
    answer = convert_int_to_str(pos)
    
    return answer

#check 함수 처럼 중첩 함수로 사용하면 solution 함수 내에 선언된 변수를 사용할 수 있음