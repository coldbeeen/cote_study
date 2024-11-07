def solution(m, musicinfos):
    answer = ''
    
    result = []
    
    for i in musicinfos:
        info = i.split(',')
        
        hour = int(info[1].split(':')[0]) - int(info[0].split(':')[0])
        minute = int(info[1].split(':')[1]) - int(info[0].split(':')[1])
        time = hour * 60 + minute #시간 환산
        
        music = list(info[-1]) #코드 저장
        
        i = 1 # '#'처리용 인덱스
        
        while (i < len(music)) and ('#' in music):
            if (music[i] == '#'): # '#'이 있을 때 리스트 내 같은 요소로 처리
                music[i - 1] = music[i - 1] + music[i]
                
                del music[i]
            else:
                i += 1

        length = len(music)
        play = music * (time // length) + music[:time % length] #음악은 재생시간만큼 반복됨
        
        m = list(m) #문자열의 각 요소를 분리
        
        i = 1 # '#'처리용 인덱스
        
        while (i < len(m)) and ('#' in m): #이전의 music처럼 똑같이 처리
            if (m[i] == '#'):
                m[i - 1] = m[i - 1] + m[i]
                
                del m[i]
            else:
                i += 1

        for i in range(len(play) - len(m) + 1):
            if (play[i : i + len(m)] == m):
                result.append([info[2], time]) #노래 제목과 재생 시간 저장
                
                break
        
    if len(result) > 0:
        result.sort(key = lambda x : x[1], reverse = True) #재생 시간으로 내림차순 정렬
        
        answer = result[0][0]
    else:
        answer = '(None)'
    
    return answer