import bisect

n = int(input())
l1 = sorted(list(map(int, input().split())))  # 정렬 수행
m = int(input())
l2 = list(map(int, input().split()))

result = []
for i in l2:
    # 이진 탐색 라이브러리를 활용해 i의 왼쪽/오른쪽 위치를 구하고 개수 계산
    cnt = bisect.bisect_right(l1, i) - bisect.bisect_left(l1, i)
    result.append(cnt)

print(*result)