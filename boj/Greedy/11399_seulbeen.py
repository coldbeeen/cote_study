import sys
n=sys.stdin.readline()
time=list(map(int,sys.stdin.readline().split()))
time.sort() #오름차순
tsum=0

for i in range(len(time)):
    tsum+=time[i]*(len(time)-i)# tsum에 현재 사람 인덱스(소요시간) * 자기포함 뒤에 남아있는 사람들 수
print(tsum)