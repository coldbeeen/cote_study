n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

start, end = 1, max(tree_list)  # 범위 정의
result = 0  # 최종적인 최댓값을 구하기 위한 변수

while start <= end:
    mid = (start + end) // 2  # 자르게 될 길이
    jaturies = sum(map(lambda tree: tree - mid if tree > mid else 0, tree_list))  # 자르고 남은 부분의 합

    if jaturies >= m:  # 잘라야 할 길이가 더 길어질 수 있음 -> 뒤 쪽 탐색
        result = max(result, mid)  # 최댓값 유지
        start = mid + 1
    else:  # (남는 부분이 더 길어져야 하므로) 잘라야 할 길이가 더 짧아야 함 -> 앞 쪽 탐색
        end = mid - 1

print(result)