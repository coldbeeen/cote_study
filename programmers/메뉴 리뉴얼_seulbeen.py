# 삼성코테에서 itertools 사용 불가하다길래 앞으로 안 써야 할 듯
from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        # defaultdict 설정 (대신 기본값을 0이 아니라 -1로)
        menu = defaultdict(lambda: -1)

        for i in range(len(orders)):
            # 사전 순으로 정렬
            orders[i] = sorted(orders[i])

            # 만들고 싶은 코스의 수보다 주문한 메뉴 수가 같거나 많아야 됨
            if len(orders[i]) >= c:
                for case in list(combinations(orders[i], c)):
                    #각각의 메뉴 조합을 str로 만들기 위해 join
                    case = "".join(case)
                    #해당 조합의 코스를 키로 가지는 value + 1
                    menu[case] += 1
        # 가장 주문이 많이 들어온 조합들을 max_menu에 넣어줌
        # 아까 default값을 -1로 해놨던 이유는 문제의 조건에 2명 이상이 주문했어야 했기 때문
        # 주석 달면서 생각해 보니까 그냥 defaultdict(int) 하고 조건문에 v>1 했으면 되네 ㅋㅋ            
        max_menu = [k for k, v in menu.items() if (max(menu.values()) == v and v > 0)]
        answer.extend(max_menu)
    return sorted(answer)
