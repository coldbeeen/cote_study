n = int(input())
solutions = list(map(int, input().split()))

left, right = 0, n-1  # 양쪽에서 시작하여 탐색
min_mixed = solutions[left] + solutions[right]  # 0과 가장 가까운 혼합된 특성값
result = solutions[left], solutions[right]  # 최종 결과 두 용액

while left < right:  # left와 right가 같아지기 전까지 반복
    mixed = solutions[left] + solutions[right]  # 혼합된 특성값 계산

    if abs(mixed) < abs(min_mixed):  # 해당 값이 0과 더 가깝다면 갱신
        min_mixed = mixed
        result = solutions[left], solutions[right]

    if mixed > 0:  # mixed 값에 따라 right, left 갱신
        right -= 1
    elif mixed < 0:
        left += 1
    else:  # 0이라면 더 이상 반복 X
        break

print(*result)