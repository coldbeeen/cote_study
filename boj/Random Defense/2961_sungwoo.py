from itertools import  combinations  # 조합 사용

n = int(input())
taste = [list(map(int, input().split())) for _ in range(n)]
min_diff = float('inf')  # 차이 최솟값

for i in range(1, n+1):  # 사용할 재료의 개수
    for comb in combinations(range(n), i):  # n개의 재료 중 개수만큼 고르기 (조합
        s, b = 1, 0
        for ingr in comb:  # 재료들을 선택해 음식의 신맛과 쓴맛을 계산
            s *= taste[ingr][0]
            b += taste[ingr][1]

        diff = abs(s - b)  # 신맛과 쓴맛의 차이 계산
        if diff < min_diff:  # 업데이트
            min_diff = diff

print(min_diff)

# combinations 안쓰고 어떻게 풀 수 있을까?
# 백트래킹 어떻게?