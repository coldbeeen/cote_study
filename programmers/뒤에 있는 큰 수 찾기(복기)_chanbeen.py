#약 58분 소요

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [] #앞서 지나간 수들이 저장되는 스택 구조
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]: #numbers[i]가 앞서 지나간 수들에게 '뒷 큰수'를 만족하는 동안
            k = stack.pop()
            answer[k] = numbers[i] #지나간 인덱스의 answer 값을 numbers[i]로 갱신
        
        stack.append(i) #현재 인덱스를 스택에 저장 후 다음으로
    
    return answer

#numbers 길이가 최대 100만, O(N^2) 알고리즘으로는 안 풀림
#스택 구조를 활용해서 해결 가능
#1. 인덱스 i를 반복적으로 스택에 저장한다
#1-1. 반복문이 진행될 수록 스택에는 앞서 지나간 인덱스들이 저장되어 있다
#2. stack이 존재하고, 가장 마지막에 지나간 인덱스 k의 값보다 현재 인덱스의 값이 크다면 뒷 큰수 조건을 만족한다
#3. k 인덱스를 pop한 뒤 answer의 k 인덱스에 현재 인덱스 값을 저장한다
#3-1. k 인덱스는 검증이 끝났고, 이전 인덱스도 확인하려는 목적으로 스택에서 pop을 해준다
#4. numbers[i]는 앞서 지나간 여러 수에게 뒷 큰수일 수 있으므로, while문으로 조건을 만족하는 동안 순회한다
#4-1. 내 차례가 지나간 후 가장 처음으로 나보다 큰 수를 저장하므로, 한 번 갱신된 뒷 큰수가 다시 갱신될 일은 없다

#다시 풀어도 스택의 선입선출 특성 때문에 코드 구현 단계에서 머리가 아팠던 문제