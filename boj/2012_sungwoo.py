import sys
input = sys.stdin.readline

n, m = map(int, input().split())

candidates = []  # 수강할 과목들의 필요한 마일리지 값 (최종 선택을 위한 후보 리스트)

for i in range(n):
    enrollNum, available = map(int, input().split())
    subjectM = sorted(map(int, input().split()), reverse=True)  # 마일리지 리스트를 내림차순 정렬한 뒤

    if available <= len(subjectM):
        candidates.append(subjectM[available - 1])  # [수강 인원 - 1] 인덱스 위치의 값이 가장 적은 마일리지로 과목을 수강하는 방법이 된다
    else:
        candidates.append(1)  # 수강 인원이 신청한 사람보다 많은 경우, 마일리지 1만 사용하면 된다

candidates.sort()  # 마일리지들을 정렬
result = 0
for i in candidates:  
    if m - i < 0:  # 마일리지 부족 시 종료
        break
    m -= i   # 마일리지가 적게 필요한 과목부터 신청하며 가용 마일리지 감소
    result += 1  # 과목 개수 증가

print(result)