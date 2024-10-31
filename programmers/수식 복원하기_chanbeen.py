def convert_to_decimal(operand, num): #주어지는 수는 음이 아닌 두 자리 이하 정수
    result = 0
    
    square = len(operand) - 1
    
    for i in range(len(operand) - 1):
        result += num ** square * int(operand[i])
        
        square -= 1
    
    return result + int(operand[-1])

def convert_to_nbase(operand, num): #n진수로 변환
    if operand == 0:
        return '0'
    
    result = ''
    
    while operand > 0:
        result = str(operand % num) + result
        
        operand //= num
    
    return result

def solution(expressions):
    answer = []

    max_num = 0
    
    for expression in expressions: #가능한 진법들 찾기 1
        num_list = []
        
        for char in expression.replace(' ', ''):
            if char.isdigit():
                num_list.extend(char)
        
        max_num = max(max([int(i) for i in num_list]), max_num)

    possible = [i for i in range(max_num + 1, 10)]
    
    flag = []
    
    for expression in expressions: #가능한 진법들 찾기 2
        if 'X' in expression:
            answer.append(expression) #답해야 하는 질문들
            continue
            
        for num in possible:
            e = expression.split(' ')
            
            A = convert_to_decimal(list(e[0]), num)
            B = convert_to_decimal(list(e[2]), num)
            C = convert_to_decimal(list(e[4]), num)
            
            if e[1] == '+': #덧셈
                if A + B != C:
                    flag.append(num)
            elif e[1] == '-': #뺄셈
                if A - B != C:
                    flag.append(num)
    
    possible = list(set(possible) - set(flag)) #flag에는 후보가 될 수 없는 숫자들이 들어있음. 기존 배열과 차집합하여 제거
    
    for i in range(len(answer)): #계산
        case = answer[i].split(' ')
        
        result = []
        
        for num in possible:
            A = convert_to_decimal(list(case[0]), num)
            B = convert_to_decimal(list(case[2]), num)
            
            if case[1] == '+':
                result.append(convert_to_nbase(A + B, num))
            elif case[1] == '-':
                result.append(convert_to_nbase(A - B, num))
        
        result = list(set(result)) 
        
        if len(result) == 1: #possible에 여러 숫자가 존재해도 계산 결과는 다 동일
            answer[i] = answer[i].replace("X", result[0])
        else: #possible에 존재하는 숫자 간 결과가 다름
            answer[i] = answer[i].replace("X", "?")     
    
    return answer

# 1. 수식에 존재하는 숫자 중 가장 높은 숫자보다 n 진법이 더 높다 (n 진법은 n를 기준으로 자리 올림하기 때문)
# Ex) 14 + 3 = 17 일 때, 이 경우에는 n은 7보다 큼 (8진법 또는 9진법)
# 2. X가 없는 연산들을 순회하면서 가능한 진법만 리스트에 추려놓기
# 이후 X를 채울 때, 후보 리스트에 가능한 진법이 하나만 있다면 값을 채우기
# 가능한 진법이 2개 이상이라면 모두 연산을 시도해보고 값이 동일하다면 그 값으로 채우고, 다르다면 ?를 채우기