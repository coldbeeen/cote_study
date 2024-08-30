def solution(sticker):

    # 크기가 2 이하라면 최댓값 리턴
    if len(sticker) <= 2:
        return max(sticker)

    # DP 테이블 생성
    # (첫 번째 원소와 마지막 원소는 함께 선택될 수 없으므로 이를 고려해 2개의 테이블 생성)
    dp = [0 for _ in range(len(sticker))]  # 첫 번째 원소 ~ 마지막 원소 이전 원소까지 다루기 위한 리스트
    dp2 = [0 for _ in range(len(sticker))]  # 두 번째 원소 ~ 마지막 원소까지 다루기 위한 리스트

    # 첫 번째 원소 ~ 마지막 원소 이전 원소까지 순회
    for i in range(len(sticker) - 1):
        dp[i] = sticker[i] + max(dp[i - 2], dp[i - 3])  # 전전/전전전 원소까지의 누적 최댓값과 현재 원소의 합을 DP 테이블에 저장

    # 두 번째 원소 ~ 마지막 원소까지 순회
    for i in range(1, len(sticker)):
        dp2[i] = sticker[i] + max(dp2[i - 2], dp2[i - 3])

    return max(max(dp), max(dp2))  # 두 DP 테이블의 모든 원소 중 최댓값 리턴