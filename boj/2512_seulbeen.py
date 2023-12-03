# 왜 안되는지 모르겠음 ㅠ 평균이 아닌건가...구글링
# 이분탐색을 인덱스로 할지 값으로 할지 생각해야됨
import sys
input=sys.stdin.readline
n=int(input())
request=list(map(int,input().split()))
budget=int(input())
# 모든 요청 배정 가능
if sum(request)<=budget:
    print(max(request))
    exit()
# 모든 요청 배정 불가능
start=0
end=max(request)
ans=float("-inf")
while start<=end:
    mid=(start+end)//2
    total=0
    for item in request:
        total+=min(item,mid)
    if total>budget:
        end=mid-1
    else:
        start=mid+1
        ans=max(ans,mid)
print(ans)
# import sys
# input=sys.stdin.readline
# n=int(input())
# request=list(map(int,input().split()))
# budget=int(input())
# # 모든 요청 배정 가능
# if sum(request)<=budget:
#     print(max(request))
#     exit()

# # 모든 요청 배정 불가능
# from bisect import bisect_left,bisect_right
# request.sort()
# nego=budget/n
# if bisect_left(request,nego)!=bisect_right(request,nego):
#     idx=bisect_right(request,nego)
# else:
#     idx=bisect_right(request,nego)

# for i in range(idx,len(request)):
#         request[i]=nego
# while True:
#     nego+=1
#     for i in range(idx,len(request)):
#         request[i]=nego
#     if sum(request)>budget:
#          nego-=1
#          break
# print(nego)