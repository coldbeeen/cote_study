import sys

input = sys.stdin.readline

N, mileage = map(int, input().split())

P = [0] * N #신청자 수
L = [0] * N #수강 가능 총 인원
Pm = [[0]] * N #신청자가 쓴 마일리지

for i in range(N):
    P[i], L[i] = map(int, input().split())
    Pm[i] = sorted(list(map(int, input().split())), reverse = True)

#전략1 : 소비한 마일리지가 같으면 성준이가 우선순위다
#전략2 : 각 과목별 막차를 탈 사람(=막차러)과 마일리지를 같게 쓰면 최소 마일리지로 수강할 수 있다
#전략3 : 과목별로 베팅 형태가 다르니, 마일리지 경쟁이 적은 과목부터 신청하자
#전략4 : 신청자 수가 수강 가능 인원보다 적다면, 마일리지를 1만 넣자
cnt = 0

target_list = []
pass_list = []

for i in range(N):
    if P[i] < L[i]: #신청자 수가 수강 가능 인원보다 적다면
        pass_list.append(i)
        if mileage > 0:
            mileage -= 1
            cnt += 1 #마일리지를 1만 써도 수강 신청 가능
    
    if i not in pass_list:
        target_idx = L[i] - 1 #과목별 막차러가 쓴 마일리지
        target_list.append(Pm[i][target_idx]) #과목별 막차러의 자리를 성준이가 뺏기

target_list.sort() #마일리지 경쟁이 적은 과목부터 신청

for i in target_list:
    if mileage < i:
        break
    mileage -= i #막차러와 같은 마일리지를 사용, 성준이가 우선순위 획득
    cnt += 1

print(cnt)