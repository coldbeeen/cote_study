# 1,2,3 더하기 4
# 1832
"""
프그에서 비슷한 느낌의 문제 풀어본거 같은데,,,
이전 숫자를 만드는 경우의수 + (새로운 케이스) 느낌의 dp로 접근하여 풀면 될 것 같다

dp[1]=1
dp[2]=2
dp[3]=3

dp[n]=d[n-1]+dp[n-2]+dp[n-3]?
근데 1+3이랑 3+1은 동일한 경우인데... 이를 어쩐담 ㅜㅜ

를 해결하기 위해서, 한번에 dp를 계산해서 더하면 안됨

n을 만드는 경우의 수= n-1을 만드는 경우의 수에 1을 더하는 경우
+ n-2를 만드는 경우의 수에 2를 더하는 경우
+ n-3을 만드는 경우의수 +3을 더하는 경우
가 아니라, n-k까지(k=2,3)의 수를 모두 1로 만드는 경우 + k를 더하는 경우라고 생각해야됨
"""
import sys
input=sys.stdin.readline

t=int(input())
nums=[]
for _ in range(t):
    nums.append(int(input()))

upper_limit=max(nums)

# 모든 숫자는 1로 제작가능
dp=[1]*(upper_limit+1)

# n-2까지의 수를 모두 1로 만드는 경우+ 2를 더하는 경우(1가지) =dp[n-2]
for i in range(2,upper_limit+1):
    dp[i]+=dp[i-2]
# n-3까지의 수를 모두 1로 만드는 경우+ 3 더하는 경우(1가지) =dp[n-3]
for i in range(3,upper_limit+1):
    dp[i]+=dp[i-3]
# print(dp)

for n in nums:
    print(dp[n])
