# 40분
# 일의자리 버튼부터 눌러서 0을 만들고 매 스텝마다 자리수를 늘려서 동일 작업 후 마지막에 가장 큰 자리수의 버튼을 눌러서 0층으로 
# 5를 기준으로 빼거나 더해서 빼는게 나을지 더하는게 나을지 판단
# 예외 케이스: 5일때를 생각 못해서 조금 시간이 걸렸다
def solution(storey):
    answer = 0
    while storey:
        # 처리해야 하는 자릿수
        remain = storey % 10

        # 5보다 큰 경우 더해서 올라감
        if remain > 5:
            storey += 10 - remain
            answer += 10 - remain
        
        # 5보다 작은 경우 빼서 내려감
        elif remain < 5:
            storey -= remain
            answer += remain
        
        # 딱 5인 경우에는 올라가나 내려가나 횟수는 똑같지만, 그 다음 자릿수를 생각해서 판단
        # ex): 35층인경우, 올라가면 40층이고 내려가면 30층 => 지금 내려가야 다음에 3번만 내려가면 됨
        else:
            # 그 다음 자릿수 
            next = (storey // 10) % 10
            # 그 다음 자릿수가 5 이상이면 올라가서 다음 자리를 6이상으로 만듬
            if next >= 5:
                storey += 10 - remain
                answer += 10 - remain
            # 그 다음 자릿수가 4이하면 내려가는게 가까움(괜히 올라가서 자리수 올리면 그만큼 더 내려가야됨)
            else:
                storey -= remain
                answer += remain
        # 0으로 만든 자릿수는 제거(자릿수가 높은 버튼을 누르는 행위를 편의를 위해 대체)
        storey //= 10
    return answer
