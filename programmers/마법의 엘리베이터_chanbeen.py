#60분 +@, 구글링

def solution(storey):
    answer = 0
    
    while storey:
        rest = storey % 10
        
        if rest < 5:
            answer += rest
        elif rest > 5:
            storey += 10 - rest #올라가야 됨
            answer += 10 - rest
        else:
            if storey // 10 % 10 >= 5:
                storey += 10 - rest
                answer += 10 - rest
            else:
                answer += rest
        
        storey //= 10
    
    return answer

#1차 제출
#10의 c제곱(c >= 0)의 버튼 존재
#재귀물을 호출하면서, 1의 자리부터 올림 또는 내림으로 처리할 생각
#기존 숫자와 올림/내림 결과 간 절댓값 연산하면 그 자리 수에서 눌러야하는 버튼 횟수 구하기 가능
#53.8점, 반례 다수 존재
#909, 4가 입력되었을 때 해당 알고리즘으로는 1010을 못 만들어서 안 풀림

#구글링
#1의 자리만 조사할 거면 재귀문 굳이 안 써도 됨, while문으로 변경
#결국 중요한 것은 각 자리 수마다 5보다 작음 / 5 / 5보다 큼을 처리해주는 것
#5일 때는 10의 자리를 봐서 5보다 같거나 크면 올려줌
#55를 반올림하면 60이 되어 올라가는 게 최단이 됨
#반대로 45를 반올림하면 50이 되어 100의 자리 수가 존재할 경우에도 내려가는 게 최단이 됨