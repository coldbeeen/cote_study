#약 38분 소요

def solution(n):
    answer = []
    
    while n:
        remainder = n % 3
        
        if remainder == 0: #3의 배수면
            remainder = 4 #4로 처리해주는 대신
            n -= 1 #숫자 1 감소 : 다음 자리 수로 이동
            
        answer.append(str(remainder))
        n //= 3
    
    answer.reverse() #마지막 자리 숫자부터 채워지므로, 뒤집어주기
    
    return ''.join(answer)

#한 자리당 1 2 4 중 하나가 위치하며, 4가 넘어갈 경우 다음 자리로 이동하는 방식
#나눗셈과 나머지를 활용하는 문제로 보임
#3진수로 바꾸는데 3의 배수면 자리수를 넘기는 대신 4를 넣어주는 느낌?

#3진수 변환 과정에서 3의 배수에 대한 처리만 해주면 무난히 통과되는 문제