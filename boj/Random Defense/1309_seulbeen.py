# 동물원
# 1시간 40분 후 구글링...
# 총 답에 9901을 나누는 건줄 알았는데 dp갱신마다 9901로 나눠줘야 메모리초과가 안남
"""
가로N 세로2 배열의 우리에 맞닿지 않게 사자배치
사자를 배치하지 않는 경우도 포함해서, 배치 할 수 있는 경우의 수
answer%=9901
"""
import sys
input=sys.stdin.readline

N=int(input())
dp=[0 for _ in range(N+1)]

# 1*2 우리에는 공백, 좌,우 3가지
if N==1:
    print(3)
    exit()

# dp배열 기본 초기화
dp[1]=3
dp[2]=7
for i in range(3,N+1):
    dp[i]=(dp[i-2]+ 2*dp[i-1])%9901
# print(dp[-1])%9901
print(dp)
# print(dp[-1])

"""
N=1
ox,xo,xx 3
N=2
xx,xx,xx
xx ox,xo

ox ox 
xx xo 

xo xo
xx ox 3+2+2

N번째 줄에 No 사자-> N-1번째까지 사자를 배치한 경우에 빈줄 추가 -> dp[N-1]

N번째 우측에 사자 -> N-1번쨰 사자가 없거나, 좌측 사자
N번째 좌측에 사자 -> N-1번쨰 사자가 없거나, 우측 사자
그런데 여기서 결국 두경우를 합쳐 생각해서 'N-1 번쨰에 사자를 안놓거나, 좌/우측에 사자'의 경우로 생각하면 -> dp[N-1]

N-1번째를 비운 상태에서 사자배치 -> dp[N-2]
"""
