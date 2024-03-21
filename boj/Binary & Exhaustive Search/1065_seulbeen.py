# 어차피 세자리수일때만 계산하면 되니까 좀 더러워도 이렇게 해야겠다
import sys
input=sys.stdin.readline
n=int(input())
if n//100==0:
    print(n)
    exit()
cnt=99
#두자리 이하일땐 무조건 등차수열

for i in range(100,n+1):
    hansu=0
    hansu+=i%10
    hansu+=i//100
    i//=10
    hansu-=2*(i%10)
    if hansu==0:
        cnt+=1
#세자리일 때도 뭐 계산 두번인거 고정이니까
print(cnt)

# 2 4 6
# 6-4=4-2
# 6-4-4+2=0

        