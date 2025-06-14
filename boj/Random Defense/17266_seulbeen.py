# 어두운 굴다리
# 2217
# 양끝에서 가장 가까운 가로등만큼의거리를 구해야 하고, 가로등끼리는 거리차이의 1/2만 있으면 커버 가능
# 완탐 아닌가? 했더니 시간초과. 이분탐색으로 조져야 할듯

import sys
import math
input=sys.stdin.readline
N=int(input())
M=int(input())
light=list(map(int,input().split(" ")))
result=M
# road=[1 if i in light else 0 for i in range(N+1)]
# 양끝에서 가장 가까운 가로등만큼의거리를 구해야 하고, 가로등끼리는 거리차이의 1/2만 있으면 커버 가능
def check(light,h):
    if light[0]>h:
        return False
    elif light[-1]+h<N:
        return False
    for i in range(M):
        if i==0:
            continue
        if math.ceil((light[i]-light[i-1])/2)>h:
            return False
    return True

start=1
end=N
while start<=end:
    mid=(start+end)//2
    # 커버가능->줄여서 테스트
    if check(light,mid):
        result=mid
        end=mid-1
    #불가능->높여서 테스트
    else:
        start=mid+1
print(result)
        