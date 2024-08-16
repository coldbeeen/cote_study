from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report_dict = defaultdict(int)
    mail_dict = defaultdict(list)
    report = list(set(report))

    for each_report in report:
        a, b = each_report.split()
        report_dict[b] += 1
        mail_dict[a].append(b)

    for id in id_list:
        cnt = 0
        for m in mail_dict[id]:
            if report_dict[m] >= k:
                cnt += 1
        answer.append(cnt)
    return answer
