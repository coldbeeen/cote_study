from collections import defaultdict

def solution(clothes):

    # 가짓 수 곱셈을 위해 1로 초기화
    answer = 1

    # 딕셔너리(Hash Map)을 생성
    cnt_by_kind = defaultdict(int)

    # 옷의 종류별 개수를 저장함
    for _, kind in clothes:
        cnt_by_kind[kind] += 1

    # 각 종류별 가짓 수를 곱셈함 (해당 종류의 옷을 선택하지 않은 것을 고려해 '개수 + 1'을 곱함)
    for kind in cnt_by_kind.keys():
        answer *= cnt_by_kind[kind] + 1

    # 아무것도 선택하지 않는 경우는 없으므로 1을 뺴줌
    return answer - 1


a = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(a))