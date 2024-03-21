
import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
dp=[-1001]*100000
dp[0]=nums[0]

for i in range(1,n):
    # 초기화해서 자신부터 시작하는게 나을지 아니면 이전까지의 최적해에 현재값을 더해서 이어나가는게 나을지 비교
    dp[i]=max(nums[i],dp[i-1]+nums[i])

print(max(dp[:n]))
"""
궁금한 점: dp배열을 입력 최대치,즉 10만으로 초기화했기 때문에 dp[:n]형태로 슬라이싱해서 max를 구하는게 더 빠를 것이라 생각했는데,
이게 웬걸? 각각 96ms, 92ms로 max(dp)가 더 빠름...왜지?"""