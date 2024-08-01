"""
처음엔 (장르 : [개별 재생횟수,고유번호])인 딕셔너리를 먼저 만들고 정렬하려 했으나 안돼서, 그냥 리스트로 먼저 받고 딕셔너리에는 (장르:총재생횟수)로 만든 후,
딕셔너리와 리스트를 비교
"""
from collections import defaultdict
def solution(genres, plays):
    answer = []
    song_dict = defaultdict(int)
    tmp_song = [[genres[i], plays[i], i] for i in range(len(genres))]
    # print(tmp_song)
    tmp_song = sorted(
        tmp_song, key=lambda x: (x[0], -x[1], x[2])
    )  # 일단 장르별 재생횟수,고유번호대로 조건에 맞게 정렬
    for x in tmp_song:
        song_dict[x[0]] += x[1]  # x[0]=장르 x[1]=재생횟수
    song_dict = sorted(
        song_dict.items(), key=lambda x: -x[1]
    )  # .items() : 딕셔너리의 키와 밸류를 튜플로
    print(song_dict)
    for items in song_dict:
        cnt = 0
        for i in tmp_song:
            if i[0] == items[0]:#딕셔너리의 장르와, 리스트의 장르를 비교
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(i[2])

    return answer
