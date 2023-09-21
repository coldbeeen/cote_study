import sys

input = sys.stdin.readline

N = int(input())
withdraw_time = list(map(int, input().split()))

total_time = 0
waiting_people = N

withdraw_time.sort()

for i in range(N):
    total_time += waiting_people * withdraw_time[i] 
    #시간은 대기자 모두 공유하므로, 대기 시간과 대기자를 곱하여 총 시간에 덧셈
    waiting_people -= 1
    #돈을 다 인출했으므로 대기자 한 명 감소
print(total_time)