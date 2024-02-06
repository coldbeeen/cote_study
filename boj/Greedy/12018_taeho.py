# 아무리 풀어도 안되서 걍 구글링했음
# 근데 문제 잘못 이해하고 있었던거
# 1이 뭔지 이해 못했는데 걍 널널한데는 1점만 넣어도 붙는거였음

import sys
import heapq

read = lambda: sys.stdin.readline().rstrip()

n, m = map(int, read().split())
answer = 0
mileages_sum = 0
subject = []

for i in range(n):
    P, L = map(int, read().split())
    mileages = list(map(int, read().split()))

    if L > P:
        heapq.heappush(subject, 1)
    else:
        mileages.sort()
        index = P - L
        heapq.heappush(subject, mileages[index])

for _ in range(len(subject)):
    mileages_sum += heapq.heappop(subject)

    if m >= mileages_sum:
        answer += 1
    else:
        break

print(answer)

'''
우선순위큐를 이용하여 문제를 풀어보았다.

신청한 사람보다 수강인원이 많을경우 subject배열에 1을 넣어준다.
마일리지를 오름차순으로 정렬하고, P-L을 index로 잡고, 입력받은 마일리지의 index값을 우선순위 큐를 이용하여 subject배열에 넣는다.
신청한 인원이 5명이고 수강인원이 4명이면 두번째로 작은 값을 구하면 된다.
오름차순으로 정렬하였으므로 가능하다.
우선순위 큐를 이용하여 pop을 하여 m값과 비교하여 합계가 m보다 작거나 같으면 과목을 1증가시키고, 아니면 종료한다.
'''