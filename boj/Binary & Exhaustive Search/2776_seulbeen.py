# 이것도 역시 set을 쓰니까 시간초과가 안뜨네... 꼼순가..?
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    note_1=set(map(int,input().split()))
    m=int(input())
    note_2=list(map(int,input().split()))
    result=[]
    for num in note_2:
        if num in note_1:
            result.append(1)
        else:
            result.append(0)
    print(*result)