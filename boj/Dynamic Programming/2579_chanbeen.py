#구글링
import sys

input = sys.stdin.readline

n = int(input())

score = [0] + list(int(input()) for _ in range(n)) + [0] * (300 - n) #총 301개의 인덱스

dp = [0] * (301) #계단은 최대 300개

dp[1] = score[1]
dp[2] = score[1] + score[2]
dp[3] = max(score[1] + score[3], score[2] + score[3]) #초기값 설정


for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])
    
print(dp[n])

#점화식
#직전에 2칸 올라왔고 이번에 1칸 올라감 vs 직전에는 상관없고 이번에 2칸 올라감
#dp[4] = max(dp[1] + score[3] + score[4], dp[2] + score[4])
#dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])