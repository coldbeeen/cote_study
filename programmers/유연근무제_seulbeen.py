# 32분
# 이벤트 실패한놈들을 세서 전체 에서 빼주자
def solution(schedules, timelogs, startday):
    answer = 0

    #문제에서 주어진 시각을 분으로 치환
    def time_convert(time_int):
        h = time_int // 100
        m = time_int % 100
        return h * 60 + m

    for i in range(len(schedules)):
        # 각 직원이 출근하겠다고 한 시각에 대한 마지노선
        event = time_convert(schedules[i]) + 10

        for j in range(7):
            # 나머지연산자활용 하여 요일관리 하기 위해 1을 빼줌(0을 만들어야해서)
            today = (startday + j - 1) % 7
            #주말은 카운트 x
            if today == 5 or today == 6:
                continue
            #출근시간이 늦었다면 이벤트 탈락
            choolgun = time_convert(timelogs[i][j])
            if event < choolgun:
                answer += 1
                break

    print(answer)

    return len(schedules) - answer
