# 9분
from collections import Counter, defaultdict
def solution(want, number, discount):
    answer = 0
    dic = defaultdict(int)
    for i in range(len(want)):
        dic[want[i]] = number[i]
        # Key:사고싶은 물건, Value: 개수
    
    for i in range(0, len(discount)):
        #10일 단위로 counter 사용하여 할인하는 물건들과 개수를 딕셔너리화
        tmp = Counter(discount[i : i + 10])
        
        #10일 딕셔너리와 구매하고싶은 물건 딕셔너리가 일치하면 answer+1
        if tmp == dic:
            answer += 1

    return answer
