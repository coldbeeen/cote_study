#약 18분 소요

def solution(numbers, target):
    def search(idx, num):
        if idx == len(numbers) and num == target: #조건 부합하는 경우
            case.append(num)
            return
        
        if idx >= len(numbers): #탐색 종료
            return
        
        search(idx + 1, num + numbers[idx])
        search(idx + 1, num - numbers[idx])
        
    case = []
    
    search(0, 0)
    
    return len(case)

#더하거나 빼거나에 대한 경우의 수를 구성하기 위해, 재귀문을 사용
#숫자의 개수가 max 20개인 덕분에, 시간 초과 발생 없이 한번에 통과(최악 477ms)