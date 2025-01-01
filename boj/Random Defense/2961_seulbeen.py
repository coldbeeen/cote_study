import sys
input=sys.stdin.readline

n=int(input())

def back_tracking(idx,s,b):
    global total
    if idx==n:
        return

    for i in range(idx+1,n):
        if not visit[i]:
            tmp=min(total,abs(s-b))
            visit[i]=True
            back_tracking(i,s*flavor[i][0],b+flavor[i][1])
            visit[i]=False
            total=min(total,tmp)
flavor=[]


visit=[False for _ in range(n)]
for i in range(n):
    m=list(map(int,input().split()))
    flavor.append(m)
total=float("inf")
for i in range(n):
    if not visit[i]:
        back_tracking(i,flavor[i][0],flavor[i][1])

print(total)