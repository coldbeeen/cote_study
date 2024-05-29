n, m = map(int, input().split())
card_list = list(map(int, input().split()))

for i in range(m):
    m1 = min(card_list)  # 첫번째 최솟값
    card_list.remove(m1)  # 첫번째 최솟값 제거
    m2 = min(card_list)  # 두번째 최솟값
    card_list.remove(m2)  # 두번째 최솟값 제거
    sum_of_two_cards = m1 + m2  # 최솟값 더하여 합친 후
    card_list.extend([sum_of_two_cards, sum_of_two_cards])  # 합친 카드 2개 삽입

print(sum(card_list))