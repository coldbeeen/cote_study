import sys
input=sys.stdin.readline
n=int(input())
dist=list(map(int,input().split()))
price=list(map(int,input().split()))

min_price=price[0]
total_price=price[0]*dist[0]

for i in range(1,len(price)-1):

    min_price=min_price if min_price<=price[i] else price[i]

    total_price+=min_price*dist[i]

print(total_price)
        