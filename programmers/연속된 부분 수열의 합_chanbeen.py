# 약 60분 소요

def solution(sequence, k):
    answer = [0, len(sequence) - 1]
    
    start = 0
    end = 0 #인덱스
    
    num = sequence[0]
    
    while True:
        if num < k:
            end += 1
            
            if end == len(sequence):
                break
            
            num += sequence[end]
        else:
            if num == k:
                if end - start < answer[1] - answer[0]:
                    answer = [start, end]
            
            num -= sequence[start]
            
            start += 1
        
    return answer

# 길이 제한이 100만, O(n^2)은 시간 초과 발생
# 투포인터로 시도
# start부터 end까지 더한 값이 k보다 큰지 작은지 비교
# 매번 덧셈을 진행하면 시간 초과 발생, 변수 하나 선언 후 그 변수에 더한 값 저장
# 더한 값이 k보다 크면, start 인덱스의 값 변수에서 빼주고 start 1 증가
# k보다 작으면, end 1 증가 후 end 인덱스의 값 변수에 덧셈
# k와 같으면, 길이 비교 후 짧을 시 answer에 저장
# end 값이 len(sequence)가 되면 break