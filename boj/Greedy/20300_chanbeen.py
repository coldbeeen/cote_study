import sys

input = sys.stdin.readline

N = int(input())
PT = sorted(list(map(int, input().split())), reverse=True)

result = []

if N % 2 != 0: #1개만 운동을 해야한다면
    result.append(PT.pop(0)) #근손실 제일 많이 나는걸로

for i in range(len(PT)//2):
    result.append(PT[i] + PT[-1 - i]) #근손실 큰거 + 적은거 로 조합
    
print(max(result)) #경우의 수 조합으로 나올 수 있는 최소 근손실값