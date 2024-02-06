import sys

input = sys.stdin.readline

n = int(input())

card = list(map(int, input().split()))

result = 0

while len(card) > 1: #카드를 합쳐주면서 최종 카드 남을 때까지
    max_level = max(card)
    max_index = card.index(max_level)
    if max_index == 0:
        another = card[max_index + 1]
    elif max_index == len(card) - 1:
        another = card[max_index - 1]
    else:
        another = max(card[max_index - 1], card[max_index + 1])
    #제일 높은 카드와 인접 카드 중 더 높은 카드를 합쳐줌
    result += (max_level + another)
    
    card.remove(another) #이후 합성에 사용한 카드는 리스트에서 삭제

print(result) 