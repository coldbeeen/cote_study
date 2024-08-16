# while문 순서 다르면 통과를 못하네;
def solution(n, t, m, timetable):

    timetable = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timetable])
    bus = [9 * 60 + i * t for i in range(n)]
    print(timetable)
    print(bus)
    idx = 0
    for b in bus:
        cnt = 0
        while cnt < m and idx < len(timetable) and timetable[idx] <= b:
        # while timetable[idx]<=b and cnt<m and idx<len(timetable): 이거 하면 list index out of range

            cnt += 1
            idx += 1
        if cnt < m:
            answer = b
        else:
            answer = timetable[idx - 1] - 1

    # for i in range()
    # print(timetable)
    # for i in range(n):

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
