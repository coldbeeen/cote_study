#약 18분 소요

from collections import deque

def solution(order):
    package = deque([i for i in range(1, len(order) + 1)]) #컨테이너 벨트
    stack = [] #보조 컨테이너
    result = [] #택배 기사님이 원하는 대로 실은 택배
    
    idx = 0
    
    while package:
        p = package.popleft()
        
        if order[idx] != p: #원하는 순서가 아닐 때
            stack.append(p) #보조 컨테이너로 직행
        else: #원하는 순서일 때
            result.append(p) #적재
            
            idx += 1

            while stack and stack[-1] == order[idx]: #보조 컨테이너가 있을 때
                result.append(stack.pop()) #보조 컨테이너에 있는 택배 중 원하는 순서와 일치하는 만큼 적재
                
                idx += 1
    
    return len(result)

#정렬된 상태로 전달
#잠시 다른 곳에 보관, 후입선출 : 스택
#길이 100만, O(n^2)이하 알고리즘 지향
#택배 상자가 [1, 2, 3, 4, 5]가 순서대로 전달되고, order에는 앞 원소의 상자부터 실어야 함
#while문으로 전달되는 택배와 보조 벨트에서 보관하는 택배를 순회

#큰 오류 없이, 무난히 통과