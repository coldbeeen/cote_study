import sys

input = sys.stdin.readline


def search_upper(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + (end - 1)) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return len(arr) - end


n, H = map(int, input().split())
seok, jong = [], []
for _ in range(n // 2):
    seok.append(int(input()))
    jong.append(int(input()))

seok.sort()
jong.sort()

result = 1e10  # 기준값
range_cnt = 0


for h in range(1, H + 1):
    seok_cnt = search_upper(seok, h - 1)
    jong_cnt = search_upper(jong, H - h)
    cnt = seok_cnt + jong_cnt

    if cnt < result:
        result = cnt
        range_cnt = 1
    elif cnt == result:
        range_cnt += 1


print(result, range_cnt)
