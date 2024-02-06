#각 과목마다 신청하면 들어갈 수 있는 마일리지 마지노선 받고 정렬?
import sys
input=sys.stdin.readline
toto=[]
n,m=map(int,input().split())

for _ in range(n):
    current_person,threshold_person=map(int,input().split())
    mileage_list=list(map(int,input().split()))
    if current_person<threshold_person:
        toto.append(1)
        continue
    mileage_list.sort(reverse=True)
    min_mileage=mileage_list[threshold_person-1]
    toto.append(min_mileage)
toto.sort()
cnt=0
for i in range(n):
    if m-toto[i]<0:
        break
    m-=toto[i]
    cnt+=1
print(cnt)

    