#약 25분 소요

def solution(k, ranges):
    answer = []
    
    n = 0
    nums = []
    
    k_copy = k #보험용 변수

    while True:
        nums.append(k_copy) #인덱스 : x좌표, 값 : y좌표로 활용
        
        if k_copy < 2 :
            break
            
        if k_copy % 2 == 0: #콜라츠 추측
            k_copy //= 2
        else:
            k_copy = k_copy * 3 + 1
        
        n += 1 #연산 횟수 카운트
    
    area = []
    
    for i in range(1, len(nums)): #각 구간별 정적분 계산(사다리꼴)
        area.append((nums[i - 1] + nums[i]) / 2)
    
    for r in ranges:
        a, b = r
        
        start = a
        end = n + b #b는 -로 주어지므로 덧셈을 해줌
        
        if start > end:
            answer.append(-1)
            continue
        elif start == end:
            answer.append(0)
            continue
            
        area_sum = 0
        
        for i in range(start, end):
            area_sum += area[i]
            
        answer.append(area_sum)
        
    return answer

#각 구역은 사다리꼴 넓이
#각 구역의 넓이 = (y좌표1 + y좌표2) * 1(x좌표 간격) / 2
#[a, -b] : x좌표가 a부터 n - b까지
#a > n - b 일 경우 -1 반환