def solution(id_list, report, k):
    answer = []
    
    report = set(report) #중복 신고 제거
    
    name_dict = {} #리폿한 id 관리
    report_dict = {} #id별 리폿당한 횟수 관리
    
    for id in id_list: #report에 등장하지 않는 id에 대해서도 생성
        name_dict[id] = []
        report_dict[id] = 0
    
    for r in report:
        left, right = r.split(' ') #left : 리폿한 id, right : 리폿당한 id
        
        report_dict[right] += 1
        name_dict[left].append(right)
    
    ban_list = []
    
    for id, cnt in report_dict.items():
        if cnt >= k:
            ban_list.append(id)
    
    for id in id_list:
        cnt = 0
        
        for i in range(len(ban_list)):
            if ban_list[i] in name_dict[id]:
                cnt += 1
        
        answer.append(cnt)
    
    return answer

# 단순 구현 문제