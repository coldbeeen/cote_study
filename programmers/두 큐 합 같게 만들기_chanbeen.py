from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    limit = len(q1) * 3
    
    while sum1 != sum2:
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            num = q2.popleft()
            q1.append(num)
            
            sum1 += num
            sum2 -= num
        
        answer += 1
        
        if answer == limit:
            return -1
        
    return answer

# sum을 반복문마다 시행하면 시간 초과
# sum 결괏값을 변수로 관리할 것
# 큐 길이가 n일 때, 반복문 횟수 제한은 3n
# (q1 -> q2) + (q2 -> q1) + (q2에 남아있던 원래 q1 -> q1) = 3n