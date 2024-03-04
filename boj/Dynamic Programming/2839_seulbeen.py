import sys
input= sys.stdin.readline

n=int(input())
#dp용 배열
dp=[float("inf") for _ in range(n+1)]
#봉지의 무게
bag=[3,5]

#dp배열 초기화
for b in bag:
    for i in range(1,n+1):
        #한 봉지들로만 채울 수 있을 때의 경우
        if i%b==0:
            if i==b:
                dp[i]=1
                continue
            # 해당 무게를 뺸 이전까지의 봉지 수 +1 (ex: i=9일 때 , i=6일 때의 봉지 수 +1개 필요)
            dp[i]=min(dp[i],dp[i-b]+1)

for i in range(1,n+1):
    for b in bag:
        # 위 초기화 식과 마찬가지. 다만 파이썬의 인덱싱때문에 배열의 뒷부분을 보게되는 경우가 생겨 i<=b라는 조건 추가
        # 봉지 무게를 뺀 이전 값이 존재한다면 그 봉지수에 1을 더하면 되고, 그렇지 않다면 정확히 킬로그램을 맞출 수 없다는 것
        if b<=i and dp[i-b]!=float("inf"):
            dp[i]=min(dp[i],dp[i-b]+1)

if dp[n]==float("inf"):
    print(-1)
else:
    print(dp[n])
            
