# 약 12분 소요

def solution(progresses, speeds):
    answer = []
    
    idx = 0
    
    while idx != len(progresses):
        cnt = 0
        
        for i in range(len(progresses)): #시간이 지날 수록 덧셈, 시간 많이 잡아먹는 부분
            progresses[i] += speeds[i]
            
        while idx < len(progresses) and progresses[idx] >= 100: #같이 배포되는 기능들 선별
            idx += 1
            cnt += 1
        
        if cnt != 0: #그 날 배포되는 기능들이 존재한다면=
            answer.append(cnt)
    
    return answer

# 먼저 배포되어야 하는 기능의 순서가 존재, 큐를 사용해야겠다고 생각
# 그러나 인덱스로 풀어보니 바로 풀렸음 (최악 0.57ms, 10.2MB)
# pop을 사용한 풀이에서는 시간이 5배정도 더 빠름 (최악 0.08ms, 10.1MB)

# pop을 사용한 풀이
# def solution(progresses, speeds):

#     answer = []
#     time = 0
#     count = 0
    
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100: 
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
            
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer