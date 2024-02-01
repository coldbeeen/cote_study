import sys
input = sys.stdin.readline

n, m = map(int, input().split())

titles = dict()
for i in range(n):
    title, power = input().split()  # 전투력을 key로, 칭호를 value로
    if int(power) not in titles:  # 중복되는 전투력 칭호 거르기
        titles[int(power)] = title

keys = list(titles.keys())
len_of_titles = len(titles)

for i in range(m):
    power = int(input())

    start, end = 0, len_of_titles - 1  # 이진탐색 수행
    while start <= end:
        mid = (start + end) // 2
        if power < keys[mid]:
            end = mid - 1
        elif power > keys[mid]:
            start = mid + 1
        else:  # 같은 경우도 내려감
            end = mid - 1

    print(titles[keys[start]])  # 최종 start 위치의 key가 해당하는 전투력임
