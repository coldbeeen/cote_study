#웅덩이가 안겹친다는 건 정렬하면 된다는 뜻인디...
#범위가 10억이라 무조건 O(N)에 끊어야 할듯
import sys
input=sys.stdin.readline
n,l=map(int,input().split())
woong=[[] for _ in range(n)]
cnt=0
for i in range(n):
    a,b=map(int,input().split())
    woong[i].append(a)
    woong[i].append(b)
woong.sort()

loc=woong[0][0]-1 #웅덩이 바로 전칸

for each in woong:
    loc=each[0]-1 if loc<each[0]-1 else loc #바로 앞에 웅덩이가 없을때 웅덩이 전까지 감
    
    gap=each[1]-1-loc # 바로 앞의 웅덩이 길이
    nul_bban_gee=(gap//l) if gap%l==0 else (gap//l)+1 #바로 앞의 웅덩이를 막기 위해 필요한 널빤지 개수
    cnt+=nul_bban_gee # 널빤지개수 카운트
    loc+=nul_bban_gee*l #널빤지 깔고 내 위치 이동
print(cnt)
        



