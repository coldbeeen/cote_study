def solution(str1, str2):

    strs = [str1, str2]
    sets = [[] for _ in range(len(strs))]

    # 각 문자열을 두 글자씩 끊어 집합을 생성
    for i in range(len(strs)):
        for j in range(len(strs[i])-1):
            tmp = strs[i][j: j+2].lower()
            if tmp.isalpha():  # 알파벳인 경우만 원소로 추가
                sets[i].append(tmp)

    # 생성한 집합들의 모든 원소를 set로 저장
    str_set = set()
    for i in range(len(strs)):
        for s in sets[i]:
            str_set.add(s)

    # 모든 원소를 순회하며, 해당 원소가 비교 대상의 문자열에 몇 개씩 포함되어 있는지 확인하면서 교집합과 합집합을 구함
    if len(str_set) != 0:
        intersection, union = 0, 0

        for s in str_set:
            intersection += min(sets[0].count(s),sets[1].count(s))
            union += max(sets[0].count(s),sets[1].count(s))

        jaccard = intersection / union  # 자카드 유사도 계산

    else:
        jaccard = 1  # 원소가 없는 경우 자카드 유사도는 1

    return int(jaccard * 65536)