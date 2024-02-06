import math

n=int(input())
list=list(map(int,input().split()))
b,c=map(int,input().split())
cnt=0
for item in list:
    if item<=b:
        cnt+=1
    else:
        cnt+=1
        item-=b
        cnt+=math.ceil(item/c)

print(cnt)