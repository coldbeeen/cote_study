# 18분
# 시키는 대로 구현하면 되는 문제

from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    days = []

    #days 배열에 각 기능을 개발하는데 소요되는 일수를 담음
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = math.ceil(remain / speeds[i])
        days.append(day)
    days = deque(days)
    
    #초기 설정
    value, max_day = 1, days[0]
    days.popleft()

    while days:
        print(days)
        print(value)
        #이전기능이 더 오래걸린다면 value +1
        if max_day >= days[0]:
            value += 1

        #아니면 그전꺼는 다 출시하면됨
        else:
            max_day = days[0]
            answer.append(value)
            print(answer)
            value = 1
        days.popleft()

    #마지막 남은 기능까지 배포
    answer.append(value)
    return answer
