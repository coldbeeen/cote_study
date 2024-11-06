# return None 인줄 알았는데 문제 보니까 "(None)"이라는 문자열을 반환하는 거였음...
# 문제에 보니까 12개가 아니라 모든 코드에 #이 있댔음...
def solution(m, musicinfos):
    answer = []

    def music_trans(music_list):
        # #붙은거를 한 문자로 치환
        result = music_list
        result = result.replace("C#", "c")
        result = result.replace("D#", "d")
        result = result.replace("F#", "f")
        result = result.replace("G#", "g")
        result = result.replace("A#", "a")
        result = result.replace("B#", "b")
        result = result.replace("E#", "e")
        return result

    def time_trans(time):
        #시간을 정수로 변환
        h, m = time.split(":")
        result = int(h) * 60 + int(m)
        return result

    def check(time,song):
        # 노래 길이가 재생시간보다 짧을경우
        if len(song) < time:
            total_song = ""
            #재생시간까지 채워서 처음부터 반복재생
            for i in range(time):
                total_song += song[i % len(song)]

        else:
            #재생시간까지만 재생
            total_song = song[:time]
        
        #최종 재생된 노래안에 기억한 멜로디가 있는지 여부 반환
        if m in total_song:
            return True
        else:
            return False

    m = music_trans(m)

    for song in musicinfos:
        # 시작시간, 끝난시간, 노래 제목, 멜로디
        s, e, name, code = song.split(",")
        
        #시간 변환
        s = time_trans(s)
        e = time_trans(e)
        
        #멜로디 치환
        code = music_trans(code)
        
        gap = e - s
        if check(gap,code):
            #나중에 정답이 여러개일수 있으니 재생시간과 시작시간도 담아둠
            answer.append([gap, s, name])
    #정답이 있을경우
    if answer:
        # 재생시간이 긴 순으로, 동일하다면 시작시간이 먼저인 순으로 정렬 후 반환
        answer.sort(key=lambda x: (-x[0], x[1]))
        return answer[0][2]
    
    return "(None)"
