def solution(cap, n, deliveries, pickups):

    i = n - 1  # 배달/수거를 수행해야 할 가장 먼 집의 위치(인덱스)이며, i를 감소시키며 진행할 것임
    result = 0

    while i >= 0:  # 모든 집의 배달/수거를 마칠 때까지 반복 (매 반복이 왕복 한 번을 의미)

        while i >= 0 and deliveries[i] == pickups[i] == 0:  # 배달/수거가 필요 없는 집은 건너뜀
            i -= 1

        result += (i + 1) * 2  # 트럭의 이동 거리 계산 후 누적

        d_cnt, p_cnt = 0, 0  # 이번 왕복에서 배달/수거할 상자 개수
        while i >= 0:  # 배달/수거 상자 개수가 cap을 초과하지 않는 범위까지 i를 감소
            if d_cnt + deliveries[i] > cap or p_cnt + pickups[i] > cap:
                break
            d_cnt += deliveries[i]
            p_cnt += pickups[i]
            i -= 1

        deliveries[i] -= cap - d_cnt  # 상자를 cap만큼 배달/수거해야 가장 효율적이므로 남은 여유분만큼 i 위치의 상자 개수를 감소
        pickups[i] -= cap - p_cnt

    return result
