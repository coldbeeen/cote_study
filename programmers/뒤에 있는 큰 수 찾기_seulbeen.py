# 2시간 후 구글링
# 반복문 돌리면 시간초과 나려나? 나네
def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = []
    for i, n in enumerate(numbers):
        print(f"i = {i} n = {n}")
        while stack and numbers[stack[-1]] < n:
            print(stack[-1])
            answer[stack.pop()] = n
        stack.append(i)
    return answer
