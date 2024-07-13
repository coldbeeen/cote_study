def solution(clothes):
    answer = 1
    cloth_dict = {}
    for cloth, category in clothes:
        if category in cloth_dict.keys():
            cloth_dict[category].append(cloth)
        else:
            cloth_dict[category] = []
            cloth_dict[category].append(cloth)
    # 가능한 경우의 수는 각 카테고리의 (의상 개수 +1(선택하지 않는, 안입는 경우)들끼리의 곱 -1)
    # -1을 하는 이유는 문제의 조건에 최소 한개의 의상은 입으므로, 아무것도 안 입는 경우 제외
    for key, values in cloth_dict.items():
        print(f"key={key},value={values}")
        answer *= len(values) + 1

    return answer - 1
