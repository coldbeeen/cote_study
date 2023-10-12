import sys
input=sys.stdin.readline
k=int(input())
chocolate_size=1
cnt=0

while chocolate_size<k: #필요한 초콜릿 길이 
    chocolate_size*=2

if chocolate_size==k: #만약에 k가 2의 거듭제곱이라면 쪼갤필요가없음 걍 지혼자 다먹으면됨
    print(f"{chocolate_size} 0")
    exit()

div_cho=chocolate_size
n=0

while n<k:
    div_cho//=2 #반으로 쪼개서
    cnt+=1# 카운트 하나 증가
    if n+div_cho > k: #만약에 정확히 k로 안떨어져서 더 쪼개야 한다면 더 잘게 쪼개야 하니까 n에 초콜릿 안 더하고 continue
        continue
    n+=div_cho
print(f"{chocolate_size} {cnt}")