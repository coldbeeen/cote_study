# 복기
# 26분
# 하 ㅅㅂ 스택사용하랬는데...
# 지난주 풀었던 '과제 진행하기'처럼, for문에서 append해놓고 while에서 작업?
def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]

    stack = []
    
    # stack에 숫자가 아닌 인덱스를 담기
    # .index() 함수로 찾으려 했는데, 숫자 중복이 있어서 의미가 없음 -> enumerate로 index를 저장
    
    # for 문에 해당하는 숫자의 인덱스를 스택에 저장
    # 다음으로 넘어가서 그 수보다 스택의 마지막값이 작다면, 스택의 마지막수 입장에서는 해당 수가'뒤에 있는 큰수'가 됨
    # 9 1 5 3 3 2 에서 포문의 n이 1이라고 가정,
    # 스택에는 [index(9),index(1)] 저장후 넘어감
    # 이제 n=5일때, 1을 pop하니, 1입장에서는 1다음의 큰수가 5인것
    for i, n in enumerate(numbers):
        while stack and n > numbers[stack[-1]]:
            idx = stack.pop()
            answer[idx] = n
        stack.append(i)

    return answer
