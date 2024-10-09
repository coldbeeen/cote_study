# 7
# 1 6, 2 5, 3 4,

# 13
# 1 12, 2 11, 3 10, 4 9, 5 8, 6 7

# 19
# 1 18 ,,,,, 9 10

# 각자 짝이 무조건 존재
# 가지고 있는 카드중에 짝이 있으면 그 라운드는 넘길 수 있음
# 짝이 있으면 코인 땡겨서 다 받아놓자

# 도저히 못풀겠어서 해설을 봤는데 포인트는 "카드를 버리는게 아니라 모아둔다"라는 거였음
# 우선순위는 필요 코인 수대로, 가지고있는 카드로 만들기 -> 가지고있던거 하나, 뽑은거 하나 -> 뽑은거 두개로 만들기
# 1 : (3,2)(1,10) 2: (2)(1,5,9) 3: (2)(5,9,8) 4: ()(5,9,8,4)
from collections import defaultdict, deque


def solution(coin, cards):
    answer = 0
    n = len(cards)
    target = n + 1
    init_card = cards[: n // 3]
    deck = deque(cards[n // 3 :])
    bbop_card = set()
    print(init_card)
    print(deck)

    while True:
        # 라운드 시작
        answer += 1

        #카드 다뽑으면 종료
        if len(deck) == 0:
            break
        #카드 두개 뽑기
        bbop_card.add(deck.popleft())
        bbop_card.add(deck.popleft())
        possible = False
        
        # 처음 카드로 만들수 있는 경우, 코인 필요 x
        for card in init_card:
            need = target - card
            if need in init_card:
                possible = True
                init_card.remove(need)
                init_card.remove(card)
                break

        if possible:
            continue

        # 원래 카드1개, 뽑은카드 1개로 만들기,코인 1개 필요
        for card in init_card:
            need = target - card

            if coin >= 1 and need in bbop_card:
                possible = True
                bbop_card.remove(need)
                init_card.remove(card)
                coin -= 1
                break

        if possible:
            continue

        # 2개로 만들기
        for card in bbop_card:
            need = target - card
            if coin >= 2 and need in bbop_card:
                possible = True
                bbop_card.remove(card)
                bbop_card.remove(need)
                coin -= 2
                break
        if possible:
            continue

        break
    return answer
