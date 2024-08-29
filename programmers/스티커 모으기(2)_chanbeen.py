def solution(sticker):
    answer = 0

    if len(sticker) == 1:
        return sticker[0]
    
    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)
    
    #첫 번째 스티커를 뜯을 때
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])
    
    #첫 번째 스티커를 뜯지 않을 때
    for i in range(1, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    
    answer = max(dp1[-2], dp2[-1])
    #첫 번째를 뜯으면 마지막꺼는 못 뜯음

    return answer