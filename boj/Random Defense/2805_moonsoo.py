

N, M = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    # mid = 절단기 높이
    mid = (start + end) // 2
    total = 0

    for tree in trees:
        # 나무가 절단기보다 높이 있으면 잘라줌
        if tree > mid:
            total += (tree - mid)
    
    if total < M:
        # 자른 나무 양이 M보다 작으면 왼쪽 이진탐색하여 더 많이 자르도록
        end = mid - 1
    else:
        # result에 결과 저장
        result = mid
        # 더 좋은 결과 있을 수 있으니 오른쪽 이진탐색
        start = mid + 1
    
print(result)