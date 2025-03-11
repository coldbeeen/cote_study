#약 27분 소요

def solution(players, m, k):
    answer = 0
    
    length = 24
    
    servers = [0] * length
    
    for idx, player in enumerate(players):
        if player // m != 0: #해당 시간은 서버가 있어야 운영 가능
            now_server = servers[idx] #현재 운영 중인 서버 수
            cnt = player // m #해당 시간 운영에 필요한 서버 수
            
            if now_server < cnt: #현재 운영 중인 서버 수가 필요한 서버 수보다 적다면
                answer += cnt - now_server #필요한 만큼 서버 증설
                
                for i in range(k): #증설한 서버는 k시간 동안 할당
                    if idx + i < length:
                        servers[idx + i] += cnt - now_server
    
    return answer

#m명 단위로 서버 1개 필요, m명 미만이면 서버 증설 필요 x
#0으로 초기화한 리스트 + 덧셈 방식으로 해당 시간 서버 수를 관리
#시간대 이용자가 m명 미만이면 서버 추가 x
#k 시간 이후에 서버 반납은 어떻게 구현하지?
#서버 수 리스트에서 k시간만큼 더해주면서 관리
#로직대로 구현하니, 무난하게 통과