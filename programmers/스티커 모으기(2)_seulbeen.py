# 경우를 나눠서 DP배열을 두개 만들생각을 못했음
def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        answer = sticker[0]
        return answer

    # 제일 처음 스티커를 떼는 경우
    dp1 = [0] + sticker[:-1]  # 마지막 스티커는 무조건 못뗌

    for i in range(2, len(sticker)):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    # 앞에서 두번째 스티커를 떼는 경우
    dp2 = [0] + sticker[1:]  # 맨 처음 스티커는 무조건 못뗌
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])

    # 두 배열의 최종 결과중 최댓값
    answer = max(dp1[-1], dp2[-1])
    return answer
