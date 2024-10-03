def solution(today, terms, privacies):

    def date_to_day(today):  # 날짜를 일(day)로 변환하는 함수
        y, m, d = map(int, today.split('.'))
        return y * 12 * 28 + m * 28 + d

    today = date_to_day(today)  # 오늘 날짜를 '일'로 변환

    term_dict = dict()  # 약관을 딕셔너리로 관리 (유효기간은 '일'로 저장)
    for term in terms:
        term_type, term_period = term.split(' ')
        term_dict[term_type] = int(term_period) * 28

    answer = []
    for i, privacy in enumerate(privacies):  # 모든 개인정보를 순회하며 유효기간 지났는지 확인
        date, term_type = privacy.split(' ')
        date = date_to_day(date)

        if today - date >= term_dict[term_type]:  # '개인정보를 보관한 기간'이 '약관의 유효기간'보다 같거나 크다면 파기
            answer.append(i+1)

    return answer