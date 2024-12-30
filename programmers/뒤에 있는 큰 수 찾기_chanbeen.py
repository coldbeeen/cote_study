#약 80분 +@, 구글링

def solution(numbers):
    stack = [] #스택 구조에는 인덱스가 들어감
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
            
        stack.append(i)
    
    return answer

# 배열 크기 100만인 것을 보고 O(n^2)로는 안 풀리겠다고 판단
# 거꾸로 푸는 것까지는 생각해서 max_num, prev_num 중 어떤 숫자를 넣을지에 대한 조건문으로 해결하려고 했음
# 샘플은 통과했지만 제출 시 대다수의 케이스에서 틀린 모습

# 구글링
# 스택 구조를 사용하는 것이 핵심
# 스택에 인덱스를 차례대로 담아주다가, numbers[i] 보다 작은 수들이 있는 인덱스를 pop하여 answer의 같은 인덱스에 numbers[i] 값을 저장하는 구조
# answer도 인덱스로 관리해주면 되기 때문에 인덱스를 스택에 저장하는 구조를 선정
# numbers의 인덱스를 담아두고, 그 인덱스들을 pop하여 answer 배열에 활용해주는 것이 인상적
# 그리디 또는 DP인 줄 알았으나, 스택이나 큐같은 구조를 활용하는 것도 중요하다는 생각  