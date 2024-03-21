# 반례 찾다가 다른 사람 코드를 봐버림...로직에 큰 힌트를 얻음
# 최댓값을 찾고 그 다음부터 최댓값을 갱신해 나가는 줄 알았는데, 시간초과가 남
# 차라리 마지막날 부터 거꾸로 와서 전날의 가격보다 비싸다면 이득보고 판거고 아니라면 최댓값 갱신 후 아무일도 없이 넘어가는 로직
import sys
input=sys.stdin.readline

t=int(input())


for _ in range(t):
    day=int(input())
    price=list(map(int,input().split()))
    max_price=price[len(price)-1]
    money=0
    for i in reversed(range(len(price)-1)):
        if max_price>price[i]:
            money+=max_price-price[i]
        else:
            max_price=price[i]
    print(money)
