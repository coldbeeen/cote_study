#약 47분 소요

def solution(diffs, times, limit):
    answer = 0
    
    wrong_case = [0] * (len(times))
    wrong_case[0] = times[0]
    
    for i in range(1, len(times)):
        wrong_case[i] = times[i - 1] + times[i] #틀렸을 때 현재 스테이지까지 돌아오는 데 걸리는 시간
    
    left = 1 #0으로 설정했더니 테스트 14에서 틀림, 문제 조건 중에 숙련도가 양의 정수여야 한다는 멘트 O
    right = 100000
    
    while left <= right:
        level = (left + right) // 2
        
        cost = 0
        
        for i in range(len(diffs)):
            if diffs[i] <= level:
                cost += times[i]
            else:
                cost += (diffs[i] - level) * wrong_case[i] + times[i]
        
        if cost > limit:
            left = level + 1
        elif cost <= limit:
            answer = level
            right = level - 1
                
    return answer

#현재 문제를 틀리면 처음부터 다시 푸는 줄 알고 wrong_case 배열을 설계했다가 시간 많이 잡아 먹었음
#숙련도가 양의 정수여야 한다는 조건 간과하여 시간 많이 잡아 먹었음