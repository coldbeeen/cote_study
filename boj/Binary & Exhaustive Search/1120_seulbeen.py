import sys
input=sys.stdin.readline
a,b=input().split()
if a in b:
    print('0')
    exit()

min_cnt=float("inf")
for i in range(len(b)-len(a)+1):
    cnt=0
    for j in range(i,i+len(a)):
        if a[j-i]!=b[j]:
            cnt+=1
    min_cnt=min_cnt if min_cnt<=cnt else cnt

print(min_cnt)