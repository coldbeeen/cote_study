#리스트의 특정 키를 기준으로 정렬하는 법 구글링 : lambda
import sys
input=sys.stdin.readline
n=int(input())
hoei=[[] for _ in range(n)]

for i in range(n):
    a,b=map(int,input().split())
    hoei[i].append(a)
    hoei[i].append(b)

hoei.sort(key=lambda x:(x[1],x[0]))# 혹은 (x[:][1],x[:][0])도 가능 , x[1]기준으로 정렬 하는데, 값이 같은 경우 x[0]기준으로 정렬한단 뜻
end_time=hoei[0][1]#가장 빨리 끝나는 회의실은 무조건 사용가능하쥐쓰 ㅋㅋ
cnt=1

for i in range(1,len(hoei)):
    if hoei[i][0]<end_time: # 만약 전 타임 회의실이 끝나는 시간 전에 싸가지 없이 예약한 놈 있으면 기각
        continue
    
    cnt+=1 #그게 아니면 cnt++ 해주고 끝나는 시간 갱신
    end_time=hoei[i][1]

print(cnt)
