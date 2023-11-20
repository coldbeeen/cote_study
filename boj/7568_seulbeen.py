import sys
input=sys.stdin.readline

n=int(input())
dungchi=[[] for i in range(n)]

for i in range(n):
    w,h=map(int,input().split())
    dungchi[i].append(w)
    dungchi[i].append(h)

#탐색하면서 키랑 몸무게 둘다 나보다 높은 사람이 있다면 내 순위가 하나씩 내려감
rank=[]
for i in range(n):
    cnt=1
    for j in range(n):
        if dungchi[i][0]<dungchi[j][0] and dungchi[i][1]<dungchi[j][1]:
            cnt+=1 
    rank.append(cnt)
print(*rank)
