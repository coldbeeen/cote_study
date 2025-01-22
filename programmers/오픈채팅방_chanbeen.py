#약 80분 소요

def solution(record):
    pre_answer = []
    answer = []
    
    event_dict = {}
    
    for r in record:
        string = r.split(' ')
        order = string[0]
        user_id = string[1]
        
        if len(string) > 2:
            nickname = string[2]
        
        if order == 'Enter':
            event_dict[user_id] = nickname
            pre_answer.append([user_id, "님이 들어왔습니다."])
            
        elif order == 'Leave':
            pre_answer.append([user_id, "님이 나갔습니다."])
            
        elif order == 'Change':
            event_dict[user_id] = nickname
    
    for pre in pre_answer:
        answer.append(event_dict[pre[0]] + pre[1])
        
    return answer

#1차 제출
#(유저 아이디, 행동, 행동 횟수)를 key로 하는 딕셔너리로 해결 시도
#별명은 변경이 가능하므로 value로 관리
#제출했으나, 케이스 하나만 맞음
#시간 초과도 발생, 'Enter'와 'Change'에서의 2중 for문에 대해서 발생한 듯
#for문을 사용하지 않고 어떻게 최신 nickname을 반영하지?
#개선 사항
#key를 user_id만 사용하고, value를 닉네임으로 사용 + for문 내에서 'Enter', 'Leave'에 따라 nickname 대신 user_id를 사용하여 result 생성
#result에 대해서 for문 돌면서 user_id가 마지막으로 설정한 닉네임으로 교체

#2차 제출
#개선 사항 반영 결과, 통과
#때로는 복잡하게 생각하는 것이 빙 돌아가는 것임을 깨달을 필요가 있음