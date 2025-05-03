# 40분
# 큐- 선입선출
# 스택- 후입선출
# 그냥 비교 하면 되는데 시간초과 뜰까봐 쫄았음
from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        #비교할 주식 pop
        joosik = prices.popleft()
        cnt = 0
        for p in prices:
            # print(f'{joosik} {p}')

            #남은 일수동안 올랐는지 떨어졌는지 체크
            if joosik <= p:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    return answer
