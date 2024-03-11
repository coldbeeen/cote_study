import sys
input=sys.stdin.readline

def square(n):
    sqrt=n**(1/2)
    # 1로 나누었을때 나머지가 0이면 정수
    if sqrt%1==0:
        return True
    else:
        return False

n=int(input())

dp=[4] * (n+1)


for i in range(1,n+1):
    if square(i):
        dp[i]=1
    else:
        for j in range(1,int(i**(1/2))+1):
            # 현 위치에서 제곱수를 뺀 수를 만들기 위한 갯수 + 제곱수 1
            dp[i]=min(dp[(i-j**2)]+1,dp[i])

            #시간 아끼려고 2면 break 걸긴 했는데 크게 유의미 한지는 모르겠음
            if dp[i]==2:
                break
print(dp[n])

