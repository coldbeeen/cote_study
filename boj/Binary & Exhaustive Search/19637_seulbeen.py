#딕셔너리로도 bisect 메소드 사용가능하려나..? 안될텐데 걍 리스트 두개 써서해야지
import sys
from bisect import bisect_left #비내림차순이고, 같으면 먼저 나온거 출력할때니까 left만 있으면 됨
input=sys.stdin.readline
n,m=map(int,input().split())
tier_name=["" for _ in range(n)] # 전투력 칭호
tier_power=[]#전투력 커트라인

for i in range(n):
    n,p=input().split()
    tier_name[i]+=n
    tier_power.append(int(p))

for _ in range(m):
    warrior=int(input())
    idx=bisect_left(tier_power,warrior)
    print(tier_name[idx])
