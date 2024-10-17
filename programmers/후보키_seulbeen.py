from itertools import combinations
def solution(relation):
    # answer에 각각의 속성 idx를 set으로 담자
    answer = []
    #행, 열 길이(생각해보니까 그냥 row, col 했으면 되네)
    rel_len = len(relation)
    attr_len = len(relation[0])
    
    #최소성 함수
    def minimal(attrs):
        # answer의 각 속성조합을 반복문으로
        for case in answer:

            # 안하면 tuple has no attribute issubset 에러 뜨더라
            case = set(case)
            
            # 부분집합이면 최소성 만족 안하는거니까 False
            # (1,2) -> (1,2,3) 이면 3 없어도 되는거니까
            if case.issubset(attrs):
                return False
        return True
    
    #희소성 함수
    def unique(attrs):

        # 릴레이션의 한 행에서, attrs안의 인덱스 행만 가져와서 set으로 바꿈(중복제거)
        # tuple()안하면 unhashable type 'list' 오류 뜸
        tmp = set([tuple([r[i] for i in attrs]) for r in relation])
        
        # 중복 제거가 된거면 False, 제거가 안되면 희소성 만족 True
        return len(tmp) == rel_len

    for i in range(attr_len + 1):
        cases = list(combinations(range(attr_len), i))
        for c in cases:
            #희소성,최소성 만족하면 append
            if unique(c) and minimal(c):
                answer.append(c)
    print(answer)

    return len(answer)
