def solution(play_time, adv_time, logs):
    answer = ""

    def transformer(time):
        hour, minute, second = time.split(":")
        cur = int(hour) * 3600 + int(minute) * 60 + int(second)
        return cur

    play_time = transformer(play_time)
    adv_time = transformer(adv_time)
    player = [0 for _ in range(play_time + 1)]

    for l in logs:
        start, end = l.split("-")
        start = transformer(start)
        end = transformer(end)
        player[start] += 1
        player[end] -= 1
    # 1111
    # 1234
    for i in range(1, len(player)):
        player[i] += player[i - 1]
    for i in range(1, len(player)):
        player[i] += player[i - 1]

    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < player[i] - player[i - adv_time]:
                most_view = player[i] - player[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < player[i]:
                most_view = player[i]
                max_time = i - adv_time + 1
    # for i in range(1,play_time):
    #     if sum(player[i:i+adv_time-1])>max_time:
    #         max_time=sum(player[i:i+adv_time-1])

    hour = max_time // 3600
    minute = (max_time % 3600) // 60
    second = (max_time % 3600) % 60
    answer = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"
    return answer
