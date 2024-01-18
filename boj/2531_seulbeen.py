import sys
input=sys.stdin.readline
n,d,k,c=map(int,input().split())
sushi=[]

for _ in range(n):
    sushi.append(int(input()))

check=len(sushi)

for i in range(k):# 원형 배열 만들기 귀찮아서 펼침
    sushi.append(sushi[i])
# right=left+k-1
# 중복을 포함 안하기 위해 각 연속된 초밥의 경우를 집합으로 만들었음
many_sushi=float("-inf")
for i in range(check):
    case=set(sushi[i:i+k])
    case.add(c)
    many_sushi=max(many_sushi,len(case))
print(many_sushi)