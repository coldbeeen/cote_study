import sys
n,k=map(int,sys.stdin.readline().split())
coin=[]
for i in range(n):
    coin.append(int(sys.stdin.readline()))

coin=tuple(sorted(coin,reverse=True)) # 내림차순 정렬이 편해서 바꾸고 튜플로 변환
cnt=0

for item in coin:
    if k//item>0:
        cnt+=k//item
        k%=item
    if k==0:
        break

print(cnt)


