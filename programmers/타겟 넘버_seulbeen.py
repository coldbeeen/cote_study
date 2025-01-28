# 50분
def solution(numbers, target):
    answer = 0

    def dfs(total, idx):
        nonlocal answer
        #배열의 끝인 경우 return
        if idx == len(numbers):
            #이때, 조건읆 만족했다면 경우의수 1 추가
            if total == target:
                answer += 1
            return
        #dfs로 모든 경우 탐색
        dfs(total + numbers[idx], idx + 1)
        dfs(total - numbers[idx], idx + 1)

    dfs(0, 0)
    return answer
