from collections import defaultdict


def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = today.split(".")
    t_y, t_m, t_d = int(t_y), int(t_m), int(t_d)

    print(f"{t_y},{t_m},{t_d}")

    terms_dict = defaultdict()
    for t in terms:
        pol, exp = t.split(" ")
        terms_dict[pol] = int(exp)
    # print(terms_dict)
    idx = 1
    for p in privacies:
        date, pol = p.split(" ")
        p_y, p_m, p_d = date.split(".")
        p_y, p_m, p_d = int(p_y), int(p_m), int(p_d)

        p_y += terms_dict[pol] // 12

        p_m += terms_dict[pol] % 12

        if p_m > 12:
            p_y += 1
            p_m -= 12
        p_d -= 1
        if p_d == 0:
            p_d = 28
            p_m -= 1
        print(f"{p_y} {p_m} {p_d}")

        if t_y > p_y:
            answer.append(idx)
        elif t_y == p_y:
            if t_m > p_m:
                answer.append(idx)
            elif t_m == p_m:
                if t_d > p_d:
                    answer.append(idx)
        idx += 1

    return answer
