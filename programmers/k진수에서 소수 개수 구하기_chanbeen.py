def solution(n, k):
    answer = 0
    
    num = ''
    
    while n > 0: #진법 변환
        num = str(n % k) + num
        n //= k
    
    num = num.split("0")
    
    for comp in num:
        if len(comp) == 0:
            continue
        if int(comp) < 2: #0 또는 1 거르기
            continue
        
        flag = 1
        
        for i in range(2, int(int(comp) ** 0.5 + 1)): #소수 탐색 범위는 제곱근까지만
            if int(comp) % i == 0:
                flag = 0
                break
            
        if flag == 1:
            answer += 1
        
    return answer