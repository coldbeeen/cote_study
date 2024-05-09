# 34퍼에서 시간초과뜸..
# ㅋㅋ 혹시몰라서 pypy3으로 하니까 되네
# start값을 0으로 하든 1로 하든 상관없네
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

trees=list(map(int,input().split()))
# print(trees)

start=1
end=max(trees)
ans=0
while start<=end:
    mid = (start + end) // 2
    length=0
    for tree in trees:
        cut= tree-mid if tree>mid else 0
        length+=cut
    if length<m:
        end=mid-1
    else:
        ans=max(ans,mid) #최적해가 존재할 수 있어서 break 걸면 안된다고 함
        start=mid+1
print(ans)
