import sys
input=sys.stdin.readline
n=int(input())
for i in range(1,n+1):
    bhh=i#자기 자신
    tmp=i
    while tmp>0:#자릿수합
        bhh+=tmp%10
        tmp//=10
    if bhh==n:
        print(i)
        exit()        
print("0")
    