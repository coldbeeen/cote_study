def solution(today, terms, privacies):
    terms_dict = {}
    
    for term in terms:
        alphabet, month = term.split()
        terms_dict[alphabet] = int(month)
    
    y, m, d = today.split('.') # 년,월,일
    today = int(str(y)+str(m)+str(d)) # 비교를 위해 int로 변환
    
    answer = []
    
    for idx in range(len(privacies)): # 각 약관마다
        privacy, alpha = privacies[idx].split() # 날짜, term
        year, month, day = map(int, privacy.split('.')) # 년,월,일
        month += terms_dict[alpha] # 알파벳에 맞게 월 증가

        if month % 12 == 0: # 12배수인 경우
            year += (month // 12) - 1
            month = 12
        else: # 12배수가 아닌 경우
            year += month // 12
            month = month % 12
        
        # int로 바꾸면서 한 자릿수가 된 month,day 조정
        year, month, day = str(year),str(month),str(day)
        
        if len(month) == 1:
            month = '0' + month
            
        if len(day) == 1:
            day = '0' + day

        # 오늘 날짜가 약관일 이상인(지난) 경우
        if today >= int(year + month + day):
            answer.append(idx+1)
            
    return answer