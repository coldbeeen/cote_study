# 50분
# 일단 성우 힌트는 공감이 안됨
# 광물을 5개마다 하나씩 묶고, 각 묶음에서 무슨 곡괭이를 쓸지 정함
# 어떤 곡괭이를 쓸지는 각 묶음에서 다이아랑 철,돌의 개수로 정함
def solution(picks, minerals):
    piro = 0
    #각 곡괭이의 개수
    dp, ip, sp = picks

    separate_list = []
    separate = []
    # 5개마다 1차원 리스트로 묶어서 append
    for idx, m in enumerate(minerals):
        if idx != 0 and idx % 5 == 0:
            separate_list.append(separate)
            separate = []
        separate.append(m)
    # 마지막 묶음(나머지로 남은 5개이하 묶음) 까지 까먹지 말고 append
    if separate:
        separate_list.append(separate)

    # 만약에 곡괭이 개수가 묶음의 개수보다 부족하다면, 뒷 묶음들은 못캠
    if len(separate_list) > sum(picks):
        separate_list = separate_list[:sum(picks)]

    #묶음 리스트를 1:다이아의 개수, 2: 철의 개수, 3:돌의 개수 우선순위로 정렬
    separate_list.sort(
        key=lambda x: (x.count("diamond"), x.count("iron"), x.count("stone")),
        reverse=True,
    )
    print(separate_list)

    for each_list in separate_list:
        for m in each_list:
            # 다이아 곡괭이 남았으면 다이아 곡괭이로 캠
            if dp > 0:
                piro += 1
            # 다이아 다 쓰고 철 곡괭이 남았으면 철곡괭이로 캠
            elif ip > 0:
                if m == "diamond":
                    piro += 5
                else:
                    piro += 1
            # 돌 곡괭이만 남았으면 돌곡괭이로 캠
            else:
                if m == "diamond":
                    piro += 25
                elif m == "iron":
                    piro += 5
                else:
                    piro += 1
        # 썼던 곡괭이 -1
        if dp > 0:
            dp -= 1
        elif ip > 0:
            ip -= 1
        else:
            sp -= 1
    return piro
