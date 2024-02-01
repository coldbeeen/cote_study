import sys
input=sys.stdin.readline
x,y,w,s=map(int,input().split())
cnt=0
if x<y: # 동일한 조건문에서 돌리기 위해 y가 더 크게 입력받을 경우 x랑 바꿔줌(도로를 직사각형으로 그렸을때 직사각형의 가로세로 모양통일)
    tmp=x
    x=y
    y=tmp

if 2*w<s: # 대각선으로 가는게 손해인 경우(즉, 수직,수평으로 한번씩 총 두번 이동할 바에 대각선이동이 더 나은경우)
    cnt=w*(x+y)
else:# 대각선으로 가야할 경우가 있는 경우
    cnt+=s*y #우선 도로의 끝까지는 최대한 대각선으로 이동
    cmp=w if w<s else s #w와 s중 이제 더 짧은 시간인걸로 이동해야됨
    if (x-y)%2==0: 
        cnt+=cmp*(x-y)
    else:#도로밖으로 대각선으로 나갔다 들어와야 하니 홀수면 못들어옴 => 나머지 한번은 어쩔수 없이 수직으로 내려와야됨
        cnt+=cmp*2*((x-y)//2)
        cnt+=w
        
print(cnt)