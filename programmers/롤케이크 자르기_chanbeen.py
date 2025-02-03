#약 22분 소요

from collections import Counter

def solution(topping):
    answer = 0
    
    top_dict = Counter(topping)
    new_dict = {}

    for i in range(len(topping)):
        elem = topping[i]
        
        top_dict[elem] -= 1
        
        if top_dict[elem] <= 0:
            del top_dict[elem]
        
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
            
        if len(top_dict) == len(new_dict):
            answer += 1
    
    return answer

#topping 배열의 길이가 최대 100만, O(n^2) 알고리즘은 통과가 안 됨
#for문 돌리면서 Set 자료형으로 개수 비교하는 게 직관적이나, 시간 초과 발생할 듯
#토핑이 정렬된 상태는 아니므로, 이진 탐색은 사용 어려움
#철수와 동생이 가진 조각의 토핑 수가 일치하는 경우가 없다 = 0 반환

#topping + Counter로 하나의 딕셔너리를 만들고, 다른 딕셔너리를 만들어서 for문으로 하나씩 채워넣는다면?
#topping 딕셔너리에서 개수가 0이 된 key는 삭제
#topping 딕셔너리의 길이와 새 딕셔너리의 길이가 같으면 answer + 1
#통과 (최악 1096.18ms)

#처음에는 케이크 전부를 동생에게 주고 철수한테 토핑 하나씩 떼주면서 토핑 종류 개수(딕셔너리의 key 개수)가 같아질 때를 세는 방법으로 접근했음