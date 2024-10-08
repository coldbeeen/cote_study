from itertools import product


def solution(n, info):
    answer = [-1]

    max_gap = 0
    # 10~0점 이니까 뒤집어서 0~10으로 맞춰줌
    info.reverse()

    # 0점부터 10점까지의 과녁에 각각 쏠래?말래?의 경우의 수들
    for c in product((True, False), repeat=11):
        # True: 내가 이 과녁에 쏴서 점수 얻을거냐? 
        # False: 이 점수는 어피치한테 쿨하게 양보하자 

        # True 들에 필요한 화살 개수 (어피치가 쏜 화살보다 한발 많게)
        arrow = sum(info[i] + 1 for i in range(11) if c[i])

        # 화살개수가 n발이거나, 남을때
        if arrow <= n:

            # 어피치가 얻은 점수 : 맞춘 과녁들중 False인 과녁 
            p = sum(i for i in range(11) if (not c[i] and info[i] != 0))
            # 라이언이 얻은 점수 : True인 과녁
            r = sum(i for i in range(11) if c[i])

            # 라이언 점수가 높은 경우
            if p < r:

                gap = r - p
                
                # 차이가 max_gap보다 클 때
                if gap > max_gap:
                    #갱신
                    max_gap = gap
                    # True(얻어야하는 점수)면 어피치보다 한발 많이 쏘고, 져도 되면 쿨하게 0으로 넘김
                    answer = [info[i] + 1 if c[i] else 0 for i in range(11)]

                    # 화살 남으면 0점에 때려박으면 됨
                    answer[0] = n - arrow
                    print(info)
                    print(answer)

                    print(f"p : {p} ryan :{r} arrow : {arrow}")

    #0~10점이니까 뒤집어서 10-0점으로 맞춰줌
    answer.reverse()
    return answer
