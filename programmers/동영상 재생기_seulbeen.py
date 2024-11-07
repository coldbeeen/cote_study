
def solution(video_len, pos, op_start, op_end, commands):
    answer = ""

    # 분:초 -> 초로 변환
    def transformer(time):
        minute, second = time.split(":")
        cur = int(minute) * 60 + int(second)
        return cur

    #오프닝 건너뛰기
    def opening(time):
        if op_start <= time <= op_end:
            return op_end
        return time

    #입력 인자들 초로 변환
    video_list = [video_len, pos, op_start, op_end]
    for i in range(len(video_list)):
        video_list[i] = transformer(video_list[i])
    video_len, pos, op_start, op_end = video_list

    #오프닝 건너뛰기
    pos = opening(pos)

    for c in commands:
        if c == "next":
            pos += 10
        else:
            pos -= 10

        if pos < 0:
            pos = 0
        if pos > video_len:
            pos = video_len
        
        pos = opening(pos)
    
    answer = f"{str(pos//60).zfill(2)}:{str(pos%60).zfill(2)}"
    
    return answer
