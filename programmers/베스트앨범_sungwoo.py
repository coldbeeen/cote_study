from collections import defaultdict

def solution(genres, plays):

    answer = []

    # 장르별 노래을 담기 위한 딕셔너리(해시 맵), 장르별 개수 리스트 생성
    genre_dict = defaultdict(list)
    genre_cnt_list = []

    # 장르별로 노래 번호와 재생 수를 추가
    for i in range(len(genres)):
        genre_dict[genres[i]].append([i, plays[i]])

    # 1. 장르별로 재생 수 기준 정렬, 2. 장르별로 총 재생 수 계산
    for genre in genre_dict.keys():
        genre_dict[genre].sort(key=lambda x: x[1], reverse=True)
        genre_cnt_list.append([genre, sum([x[1] for x in genre_dict[genre]])])

    # 장르별 총 재생 수 기준 정렬
    genre_cnt_list.sort(key=lambda x: x[1], reverse=True)

    # 가장 많이 재생된 장르부터 순회, 장르별 가장 많이 재생된 노래 최대 2곡 answer에 추가
    for genre, _ in genre_cnt_list:
        top2 = genre_dict[genre][:2]
        answer.extend([x[0] for x in top2])

    return answer