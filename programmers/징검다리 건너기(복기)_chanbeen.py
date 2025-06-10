#60분 +@, 구글링(이진 탐색)

def solution(stones, k):
    answer = 0
    
    left = 1
    right = 200000000 #stones 배열 원소 최댓값
    
    while left <= right:
        mid = (left + right) // 2
        
        cnt = 0
        
        for i in range(len(stones)):
            if stones[i] - mid <= 0: #mid 명이 건널 경우 연속으로 0이 되는 돌 개수 카운트
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k: #k보다 cnt가 커져서 못 건너뛰게 됨
                break
        
        if cnt >= k: #mid 명이 건너는 것은 불가능, 값 범위 낮추기
            right = mid - 1
        else: #mid 명이 건너는 것은 가능, 값 범위 높이기
            left = mid + 1
    
    return left

#각 친구는 최대 k칸을 건너뜀
#각 디딤돌은 숫자를 가지고 있으며, 한 번 밟힐 때마다 -1
#디딤돌 숫자가 0이 되면 그 디딤돌은 더 이상 사용 불가
#0인 디딤돌이 연속으로 k개 이상이면 더이상 징검다리를 건너갈 수 없음
#idx를 1씩 증가시켜가며, idx 이하의 값이 연속 k번 이상 등장하는 최초의 idx를 찾아 answer로 반환?

#1차 제출
#정확성은 다 통과하나, 효율성에서 전부 시간 초과
#while True + for문 하니까 시간 초과, 2중 반복문으로는 못 푸는 문제

#구글링
#stones 배열 원소 최댓값이 2억이므로, 건널 수 있는 친구들도 최대 2억명
#mid 명을 통과시키는 시나리오가 가능한지 검증하며 최댓값을 계속 갱신하는 이진 탐색 적용

#이진 탐색을 리마인드하기 좋은 문제