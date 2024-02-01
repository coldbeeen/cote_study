# 합성의 기준이 되는 카드는 소멸안되고 살아남음 => 가장 큰애가 계속 살아남는게 최대이득
import sys
input=sys.stdin.readline
n=int(input())
card=list(map(int,input().split()))
gold=0

if n==1: #하나밖에 없으면 조건문 안들가고 걍 카드 레벨 출력
    print(card[0])
    exit()
while len(card)>1: #카드 하나남을때 까지
    max_card=card.index(max(card))
    if max_card==0: # 맨 왼쪽인 경우에 다음 카드를 재료로 써서 합성하고 카드소멸
        gold+=card[max_card]+card[1]
        card.pop(1)
    elif max_card==len(card)-1: #맨 끝인 경우에 이전 카드를 재료로 써서 합성하고 카드소멸
        gold+=card[max_card]+card[max_card-1]
        card.pop(max_card-1)
    else:#가운데 경우에 처음에는 양옆의 대소관계도 고려해야한다고 생각했는데 다시 생각해보니 상관없음. 걍 제일 큰애 기준으로 양옆 아무거나 계속 합성하면됨
        gold+=card[max_card]+card[max_card-1]#난 그냥 이전껄로 함
        card.pop(max_card-1)
print(gold)

