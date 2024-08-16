from collections import defaultdict

def solution(id_list, report, k):

    # 유저별로 신고한 사용자 Set를 저장하는 'report_dict' (HashMap<String, HashSet>)
    # 유저별로 신고된 횟수를 저장하는 `cnt_dict` (HashMap<String, Integer>)
    report_dict = defaultdict(set)
    cnt_dict = defaultdict(int)

    # 유저별로 신고한 사용자 저장 (Set이므로 한 유저가 여러 번 신고한 건에 대해서는 한 번만 적용)
    for r in report:
        reporter, reportee = r.split(' ')
        report_dict[reporter].add(reportee)

    # 유저별로 신고된 횟수 계산
    for reportees in report_dict.values():
        for reportee in reportees:
            cnt_dict[reportee] += 1

    # id_list에 저장된 id 순서로, 신고한 유저에 대한 정지 처리 결과 메일을 받은 횟수를 answer에 저장
    answer = []
    for reporter in id_list:

        report_cnt = 0
        for reportee in report_dict[reporter]:
            if cnt_dict[reportee] >= k:
                report_cnt += 1

        answer.append(report_cnt)

    return answer