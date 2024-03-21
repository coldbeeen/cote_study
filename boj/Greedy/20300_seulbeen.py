import sys
input=sys.stdin.readline
n=int(input())
gym=list(map(int,input().split()))
gym.sort()
min=float("-inf")
if len(gym)%2==0:
    for i in range(len(gym)//2):
        sonsil=gym[i]+gym[-(1+i)]
        min=sonsil if min<sonsil else min
else:
    for i in range(len(gym)//2):
        sonsil=gym[i]+gym[-(2+i)]
        min=sonsil if min<sonsil else min
    min=min if gym[-1]<min else gym[-1]
print(min)

# 일단 오름차순 정렬, 제일 근손실 많은애랑 적은애를 묶어서 운동
# 근데 만약에 기구를 하나 쓰는 상황이 생긴다면? 제일 근손실 큰애를 마지막날 하나만 쓰고 나머지 애들끼리 두개 묶음