# 유명한 dp문제라고 하니 알아두자...(LIS : Longest Increasing Sequence)
import sys
input=sys.stdin.readline

n=int(input())

nums=list(map(int,input().split()))
#자기 자신만 원소로 가지는 수열이 최솟값이기 때문에 1로 초기화
dp=[1]*1000

for i in range(1,n):
    for j in range(i):
        # 증가하는 수열 조건을 만족하기 위한 조건문
        if nums[i]>nums[j]:
            #이전 값들을 비교하면서 현재값과 이전 시퀀스에 자기자신을 연결하는 것중 대소비교
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))