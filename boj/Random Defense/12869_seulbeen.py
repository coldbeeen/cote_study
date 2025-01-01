import sys
input=sys.stdin.readline

n=int(input())
scv=list(map(int,input().split()))
total=float("inf")
flag=len(scv)
def dfs(one,two,three,count):
    global total
    if count > total:
        return
    if one<0:
        one=0
    if two<0:
        two=0
    if three<0:
        three=0

    if one==0 and two ==0 and three==0:
        total=min(count,total)
        return
    if flag==1:
        
    dfs(one - 9, two - 3, three - 1, count + 1)
    dfs(one - 9, two - 1, three - 3, count + 1)
    dfs(one - 3, two - 9, three - 1, count + 1)
    dfs(one - 3, two - 1, three - 9, count + 1)
    dfs(one - 1, two - 3, three - 9, count + 1)
    dfs(one - 1, two - 9, three - 3, count + 1)
dfs(scv[0],scv[1],scv[2],0)
print(total)
# cnt=0

# total_hp=sum(scv)

# if n==3:
#     divide=13
# elif n==2:
#     divide=12
# else:
#     divide=9

# cnt=total_hp//divide if total_hp%divide==0 else total_hp//divide +1
# print(cnt)
