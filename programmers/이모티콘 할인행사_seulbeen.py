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
        cnt, price = 0, 0
        for i in range(len(users)):
            user_dis = users[i][0]
            total = 0

            for j in range(len(p)):
                if user_dis <= p[j]:
                    total += emoticons[j] * (100 - p[j]) * 0.01

            if total >= users[i][1]:
                cnt += 1

            else:
                price += total

        if answer[0] > cnt:
            continue

        if answer[0] == cnt and answer[1] > price:
            continue

        answer = [cnt, price]

    return answer
