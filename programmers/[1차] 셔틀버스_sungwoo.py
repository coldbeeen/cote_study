from heapq import *

def to_answer(minute):
    answer_h, answer_m = minute // 60, minute % 60
    return f"{answer_h:02}:{answer_m:02}"

def solution(n, t, m, timetable):

    # 계산 및 비교를 위해 분 단위로 변환
    times = []
    for time in timetable:
        hour, minute = time.split(':')
        times.append(int(hour) * 60 + int(minute))

    # 최소힙을 활용해 효율적으로 최솟값을 pop하도록 할 것임
    heapify(times)

    # 셔틀 시작 시간 설정
    h = 540  # 09:00 -> 540 min

    # 셔틀 운행 횟수만큼 반복하며 크루를 태움. 동시에 셔틀 시간 h를 관리함
    for i in range(n):

        # m명의 크루를 탑슴 시킴
        for j in range(m):

            if len(times) == 0:  # 더 이상 크루가 없는 경우 해당 셔틀 시간에 탑승
                return to_answer(h)

            if times[0] > h:  # 크루 도착 시간 최솟값이 h보다 크다면 (더 이상 태울 수 없다면) 탑승 종료
                break

            if i == n - 1 and j == m - 1:  # 이번 크루가 가장 마지막 탑승자라면 '해당 크루의 탑승 시간 - 1'에 탑승
                return to_answer(times[0] - 1)

            heappop(times)  # 위 조건문들이 해당되지 않는다면 '도착 시간이 최솟값인 크루'를 탑승시킴

        h += t  # 다음 셔틀 시간

    # times[0] > h인 크루가 남아 있는 상태 (동시에 마지막 탑승자가 결정되지 않은 상태)
    # 이 경우는 가장 마지막 셔틀 시간에 탑승 시키면 된다.
    return to_answer(h - t)