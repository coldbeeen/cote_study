#삼중포문 쓰는거 맞나 싶긴한데 어차피 다 탐색해야될거같은디
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
blackjack=list(map(int,input().split()))
max=0
for i in range(len(blackjack)):
    for j in range(i+1,len(blackjack)):
        for k in range(j+1,len(blackjack)):
            sum=blackjack[i]+blackjack[j]+blackjack[k]
            if sum<=m:
                max=sum if max<sum else max
print(max)
