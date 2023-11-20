import sys
input=sys.stdin.readline

n=int(input())
cnt=0

i=0
while True:
    if cnt==n:# n번째 재앙의 수 도달하면 나옴
        break
    i+=1
    if "666" in str(i): # 재앙의 수면 카운트 1증가
        cnt+=1
    
print(i)
