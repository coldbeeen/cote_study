n, m = map(int, input().split())
lectures = list(map(int, input().split()))

# left(가능한 최솟값)은 가장 긴 강의 길이, right(가능한 최댓값)은 모든 강의 길이 합으로
start, end = max(lectures), sum(lectures)

while start <= end:
    mid = (start + end) // 2

    tmp_length = 0  # 한 블루레이에 담을 강의 길이 임시 변수
    tmp_blueray_cnt = 0  # 블루레이 개수 카운트 임시 변수
    for lecture in lectures:  # 강의를 순회하면서
        if tmp_length + lecture > mid:  # 한 블루레이에 더 이상 담지 못한다면 다음 블루레이로
            tmp_length = 0
            tmp_blueray_cnt += 1
        tmp_length += lecture
    tmp_blueray_cnt += 1  # 남은 강의까지 해서 블루레이 개수 1개 추가

    if tmp_blueray_cnt <= m:  # 가능함. start ~ mid-1로 범위 좁힘
        end = mid - 1
    else:  # 불가능. mid+1 ~ end로 범위 좁힘
        start = mid + 1

print(start)