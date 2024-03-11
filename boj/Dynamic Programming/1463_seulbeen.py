import sys
input=sys.stdin.readline

n=int(input())


dp=[float("inf")] * (n+1)
nums=[2,3]
dp[0]=0
dp[1]=0
for i in range(2,n+1):
    for num in nums:# 2,3 으로 나누어 떨어지는지 검사
        #2,3으로 나누어 떨어지는 수라면, 2,3으로 나눈 수를 1로 만드는데 드는 횟수 + 2,3으로 나누는 1회 추가
        if i%num==0:
            dp[i]=min(dp[i//num]+1,dp[i])
        else:
            dp[i]=min(dp[i],dp[i-1]+1)
print(dp[n])