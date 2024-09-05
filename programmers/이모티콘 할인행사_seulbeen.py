from itertools import product
# product : 리스트의 카테시안 곱을 반환
# product("12","34") => 13,14,23,24
# repeat : 한리스트를 n만큼 반복해서 동일 진행
# product("12",repeat=2) = product("12","12")

def solution(users, emoticons):
    emg_len = len(emoticons)
    answer = [0, 0]
    dis = [10, 20, 30, 40]
    for p in product(dis, repeat=emg_len):
        counts, money = 0, 0
        for i in range(len(users)):
            user_discount = users[i][0]
            total = 0

            for j in range(len(p)):
                if user_discount <= p[j]:
                    total += emoticons[j] * (100 - p[j]) * 0.01

            if total >= users[i][1]:
                counts += 1

            else:
                money += total

        if answer[0] > counts:
            continue

        if answer[0] == counts and answer[1] > money:
            continue

        answer = [counts, money]

    return answer
