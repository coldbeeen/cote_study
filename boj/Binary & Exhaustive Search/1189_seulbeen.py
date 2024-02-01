# 어차피 오른쪽, 위로만 가야 같은 곳 안가고 최단거리임
import sys
input=sys.stdin.readline
r,c,k=map(int,input().split())
road=[str(input().rstrip()) for _ in range(r)]
#좌표 기준 상하좌우 경우의 수를 배열로
row=[-1,1,0,0]
col=[0,0,-1,1]
# 못가는 곳이나 방문 했던 곳은 True
visit=[[False]*c for _ in range(r)]
visit[r-1][0]=True
for i in range(r):
    for j in range(c):
        if road[i][j]=='T':
            visit[i][j]=True
cnt=0
distance=1
def case(r_idx,c_idx,distance):
    global cnt
    if r_idx==0 and c_idx==c-1: # 종료조건 : 끝까지 갔을때 종료, 원하는 거리까지 맞으면 카운트 1증가
        if distance==k:
            cnt+=1       
        return
    for i in range(4): # 상하좌우
        next_row=r_idx+row[i]
        next_col=c_idx+col[i]
        if 0<= next_row < r and 0<= next_col< c and visit[next_row][next_col]==False and distance < k : # 다음 좌표가 이동가능할 경우이면서 이동할 거리도 남았을 때
            visit[next_row][next_col]=True
            case(next_row,next_col,distance+1)
            visit[next_row][next_col]=False

    
    
        

case(r-1,0,distance)
print(cnt)

        