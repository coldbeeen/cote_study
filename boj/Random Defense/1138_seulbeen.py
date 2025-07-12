#한줄로 서기
#17분
"""
1번아이부터 순서대로 각자 자신 기준으로 왼쪽에 자기보다 큰애가 몇명있는지?
그러면 그냥 문제의 조건에 맞게 시키는대로 줄을 세우면 됨
1번부터 세울거니까 어차피 자기 앞에 누군가 있다면, 이미 나보다 작은애인것 
"""
import sys
input=sys.stdin.readline
N=int(input())
info=[0]+list(map(int,input().split()))
result=[0 for _ in range(N)]
# print(info)

for i in range(1,N+1):
    cnt=0
    for j in range(N):
        # 빈자리이고, cnt랑 자기보다 큰 사람 수랑 같으면 본인자리임
        if result[j]==0 and cnt==info[i]:
            result[j]=i
            break
        # 빈자리라면 cnt+1 (빈자리가 아니라는건, 자기보다 작은애가 이미 있다는거니까)
        elif result[j]==0:
            cnt+=1

print(*result)
