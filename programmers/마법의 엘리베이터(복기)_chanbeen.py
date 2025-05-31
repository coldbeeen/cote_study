#약 41분 소요

def solution(storey):
    answer = 0
    
    while storey:
        rest = storey % 10
        
        if rest < 5:
            storey -= rest
            answer += rest #내려감
        elif rest > 5:
            storey += 10 - rest #올라감
            answer += 10 - rest
        else:
            if storey // 10 % 10 < 5: #앞 숫자 보고 판단
                storey -= rest
                answer += rest
            else:
                storey += 10 - rest
                answer += 10 - rest
        
        storey //= 10
    
    return answer

# +- 1, +- 10, +- 100, ... 의 형태로 이동할 수 있음
#0에 도착하면 종료
#십의 자리수 단위로 이동하므로, 나머지로 해결하는 것이 효과적임
#나머지가 5보다 작으면 내려가고, 5보다 크면 올라간다

#나머지가 정확하게 5일 때는?
#45일때는 내려가는 게 낫고, 65일때는 올라가는 게 낫다
#55일때는 어디로 가든 0까지 걸리는 횟수는 똑같다

#5일 때는 앞 숫자를 보고 판단하는 게 맞다

#나머지가 5이고 앞 숫자가 없는 케이스도 반영이 되나?
#storey // 10 % 10 하면 0이 나올테니 반영이 됨