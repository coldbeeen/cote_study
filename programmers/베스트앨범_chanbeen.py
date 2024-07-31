def solution(genres, plays):
    answer = []
    
    genre_dict = {} # 장르별 노래 고유 번호 저장
    plays_dict = {} # 장르별 재생 횟수 저장
    
    for i in range(len(genres)):
        if genres[i] not in plays_dict.keys():
            plays_dict[genres[i]] = 0
            
        plays_dict[genres[i]] += plays[i]
        
        if genres[i] not in genre_dict.keys():
            genre_dict[genres[i]] = []
        
        genre_dict[genres[i]].append([i, plays[i]]) #[고유번호, 재생 횟수]를 저장
    
    genre_list = list(dict(sorted(list(plays_dict.items()), key = lambda x: x[1], reverse = True))) #재생 횟수가 많은 장르 순으로 정렬
    
    for g in genre_list: #재생 횟수가 많은 장르부터 돌면서
        genre_dict[g] = sorted(genre_dict[g], key = lambda x: x[1], reverse = True) #장르 내에서 재생 횟수 큰 순으로 정렬
        
        answer.append(genre_dict[g][0][0])
        
        if len(genre_dict[g]) > 1:
            answer.append(genre_dict[g][1][0]) #장르당 pop 2번까지만
    
    return answer