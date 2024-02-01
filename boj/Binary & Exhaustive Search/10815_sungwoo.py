n = int(input())
nNums = sorted(list(map(int, input().split())))  # 정렬 수행
m = int(input())
mNums = list(map(int, input().split()))

for mNum in mNums:
    # 이진 탐색 수행
    start, end, result = 0, n-1, 0
    while start <= end:
        mid = (start + end) // 2
        if nNums[mid] > mNum:  # 왼쪽에 있다면
            end = mid - 1
        elif nNums[mid] < mNum:  # 오른쪽에 있다면
            start = mid + 1
        else:  # 찾았다면
            result = 1
            break

    print(result, end=' ')
