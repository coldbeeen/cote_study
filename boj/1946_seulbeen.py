# 일단 기준 하나 정해서 한종목으로 정렬 후에 다른 종목 순위 비교로 ㄱㄱ (앞순위 애한테 다른종목까지 지면 나가리)
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    test=[[]for _ in range(n)]

    for i in range(n):
        a,b=map(int,input().split())
        test[i].append(a)
        test[i].append(b)
    
    test.sort(key=lambda x:x[0])
    good=test[0][1]
    cnt=1
    
    for i in range(1,n):
        if test[i][1]<good:
            cnt+=1
            good=test[i][1]
    print(cnt)