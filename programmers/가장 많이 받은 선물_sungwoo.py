def solution(friends, gifts):

    friend_dict = {friend: i for i, friend in enumerate(friends)}  # 친구 이름을 인덱스로 대응시키기 위한 딕셔너리(HashMap)
    gift_matrix = [[0 for _ in range(len(friends))] for _ in range(len(friends))]  # 주고 받은 선물에 대한 행렬

    # 선물 행렬 생성
    for gift in gifts:
        giver, taker = map(lambda friend: friend_dict[friend], gift.split())
        gift_matrix[giver][taker] += 1

    # 선물 지수 구하기
    gift_index = [0 for _ in range(len(friends))]
    for idx in range(len(friends)):
        give_cnt = sum(gift_matrix[idx])
        take_cnt = sum([row[idx] for row in gift_matrix])
        gift_index[idx] = give_cnt - take_cnt

    # 받을 선물 개수 구하기
    take_result = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:  # 같은 사람은 건너뛰기
                continue

            # 선물을 더 많이 줬거나, 개수가 같으면서 선물 지수가 더 높다면 -> 선물을 받게 됨
            if (gift_matrix[i][j] > gift_matrix[j][i] or
                    gift_matrix[i][j] == gift_matrix[j][i] and gift_index[i] > gift_index[j]):
                take_result[i] += 1

    return max(take_result)