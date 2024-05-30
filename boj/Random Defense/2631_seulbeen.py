#LIS 응용
import sys
input=sys.stdin.readline

kids=[]
n=int(input())
dp=[1 for _ in range(n)]
for _ in range(n):
    kids.append(int(input()))

#dp[k]에 담기는 값은 k번쨰 원소를 마지막으로 가지는 가장 긴 증가하는 수열의 길이
for i in range(1,n):
    for j in range(i):
        # j번째 보다 i번째가 크다면
        if kids[j]<kids[i]:
            #max(현재 i번째를 마지막으로 가지는 수열 길이,j번째를 마지막으로 가지는 증가하는 수열의 길이 + 자기자신)
            dp[i]=max(dp[i],dp[j]+1)
""" 
이렇게 하면 max(dp) : 가장 긴 증가하는 부분수열의 최대길이
 => 최대 길이에 포함되는 애들만 남기고 나머지를 이동시키면 그게 최소 횟수일 것
"""
result=n-max(dp)
print(result)