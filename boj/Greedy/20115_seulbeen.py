#흘리는게 적어야 한다는 소리니까 정렬하고 적은애부터 젤 큰 애한테 합치자
import sys
input=sys.stdin.readline
n=int(input())
energy=list(map(float,input().split()))
energy.sort()
for i in range(len(energy)-1):
    energy[-1]+=energy[i]/2
    energy[i]=0
print(energy[-1])