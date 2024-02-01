# 처음에 이진탐색인줄 모르고 in 써서 풀었다가 시간초과
# 그래서 이진탐색으로 풀었는데도 시간초과
# 근데 이게 웬걸... 처음에 푼 방식을 set(집합)을 쓰면 시간초과가 안뜸 ㄷㄷ in으로 탐색하는 방식이 다르다고 함(해시테이블)
# result 출력할때 *result하면 언패킹되면서 자동으로 공백두고 출력해줌 ㄷㄷ
import sys
input=sys.stdin.readline

n=int(input())
s_card=set(map(int,input().split()))
m=int(input())
c_card=input().split()
result=[]
for check in c_card:
    if int(check) in s_card:
        result.append("1")
    else:
        result.append("0")
print(*result)


# def binary_search(l,target):
#     if len(l)==0:
#         return 0
#     mid=len(l)//2
#     if target==l[mid]:
#         return 1
#     elif target<l[mid]:
#         return binary_search(l[:mid],target)
#     else:
#         return binary_search(l[mid+1:],target)

# n=int(input())
# s_card=list(map(int,input().split()))
# s_card.sort()
# m=int(input())
# c_card=list(map(int,input().split()))
# c_card.sort()

# result=[]
# for card in c_card:
#     result.append(binary_search(s_card,card))
# print(*result)
