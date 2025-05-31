# 14분
"""
10층을 내려가든 1층을 내려가든 100층을 내려가든 사용하는 돌은 1개임
자릿수마다 5를 기준으로 5보다 작으면 내려가고, 5보다 크면 올라가는게 더 효율적
딱 5일때는, 그 다음자리수를 보고 판단해서 내려가는게 나을지 올라가는게 나을지 판단
ex) 165 -> 올라가서 170층으로 만듦 -> 200층 -> -200층
ex) 125 -> 내려가서 120층으로 만듦(올라가면 130층이라서 한번 더 내려가야됨) -> -20 -> -100
"""
def solution(storey):
    answer = 0

    while storey:
        # 가장 작은 자리 수 계산
        rest = storey % 10

        # 5층인 경우
        if rest == 5:
            # 다음자리 수
            tmp = (storey // 10) % 10

            #다음자리가 1,2,3,4면 내려가는게 이득
            if tmp < 5:
                storey -= rest
                answer += rest
            # 5,6,7,8,9면 올라가는게 이득
            else:
                storey += 10 - rest
                answer += 10 - rest
        # 6,7,8,9 층 일때는 올라감
        elif rest > 5:
            storey += 10 - rest
            answer += 10 - rest
        # 1,2,3,4 층일때는 내려감
        elif rest < 5:
            storey -= rest
            answer += rest
        storey //= 10

    return answer
