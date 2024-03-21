# ㅋㅋ 이렇게 푸는게 맞나 싶은데, 최소 울타리 개수를 구하는게 아니라서 그냥 양의 주위를 울타리로 감싸버렸음
import sys
input=sys.stdin.readline
r,c=map(int,input().split())
mokjang=[[] for _ in range(r)]
flag=1

def wooltari(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<c and 0<=ny<r:
            if mokjang[ny][nx]=='W': # 양과 인접한 칸에 늑대 있으면 울타리 설치 못하고 막을 수 없음
               return 0
            if mokjang[ny][nx]=='.':# 양과 인접한 칸이 빈칸이면 울타리 설치
                mokjang[ny][nx]='D'
            
    return 1    
for i in range(r):
    mokjang[i].extend(input().rstrip())
    
for y in range(r):
    for x in range(c):
        if mokjang[y][x]=='S':
            flag=wooltari(x,y)
            if not flag:# 늑대를 못 막을시 0 출력 후 종료
                print(flag)
                exit()
print(flag)
for y in range(r):
    for x in range(c):
        print(mokjang[y][x],end='')
    print()
  