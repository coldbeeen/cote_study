n=int(input())
a=list(map(int,input().split()))
b, c=map(int,input().split())

cnt=0

for i in range(n):
    a[i] -= b
    cnt += 1
    if a[i]>0:
        if a[i] % c == 0:
            cnt+=(a[i]//c)
        else:
            cnt+=(a[i]//c+1)

print(cnt)