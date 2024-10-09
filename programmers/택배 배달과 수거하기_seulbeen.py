# 거꾸로 풀기
# 어차피 배달이든 수거든 뭐가 남아있으면, 들르긴 해야됨
# 갔으면, 그만큼 돌아 와야됨
# 갈때 수거랑 배달을 동시에 할 수도 있다고 생각했는데, 어차피 똑같음,,, 갈떄는 배달, 올 때는 수거
#
# 1 0 3 1 2
# 0 3 0 4 0

# 5번째에서 두개 배달, 0개 수거
# 4번째에서 1개 배달 4개 수거


def solution(cap, n, deliveries, pickups):

    answer = 0
    dv = 0
    pu = 0

    for i in range(n - 1, -1, -1):
        dv -= deliveries[i]
        pu -= pickups[i]
        cnt = 0

        while dv < 0 or pu < 0:
            dv += cap
            pu += cap
            cnt += 1

        answer += 2 * cnt * (i + 1)
    return answer
