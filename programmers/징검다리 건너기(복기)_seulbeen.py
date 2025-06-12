# 효율성 14번 해결이 안됨...ㅠ
"""
대충 구현하니 몇개 틀리고 시간초과나고 난리도 아님
원소들의 값이 최대 2억,,, 배열의 크기가 20만,,,
저번엔 이분탐색으로 풀었는데, 슬라이딩윈도우가 좋다..?
"""
from collections import deque
"""
길이가 k인 슬라이딩 윈도우 내에서의 최댓값들을 구하고, 그중 가장 작은 값이 정답임
그 값보다 작아져 버리면 해당 슬라이딩윈도우 내의 모든 값이 0이하로 내려가기 때문에 k이상 건너뛸 수가 없음
"""
def solution(stones, k):
    max_sliding_window = []
    result = 200000000
    q = deque()
    # stones의 길이가 1개일때는 그 돌의 숫자만큼 건널 수 있음
    if len(stones) == 1:
        return stones[0]
    
    for idx, num in enumerate(stones):
        # q안에는 돌의 값이 큰 순서대로 정렬되어있고, 그 돌의 인덱스를 저장
        #
        while q and stones[q[-1]] <= num:
            q.pop()
        q.append(idx)
        
        #가장 왼쪽의(제일 큰) 값의 인덱스가 윈도우 범위 밖을 벗어난다면, popleft 
        while idx - q[0] + 1 > k:
            q.popleft()

        # k까지 슬라이딩윈도우가 확장되지 않았다면 append하지 않음
        if idx > k:
            # result=min(result,stones[q[0]])
            max_sliding_window.append(stones[q[0]])
    # return result
    # return min(max_sliding_window)
    # print(max_sliding_window)
    return min(max_sliding_window)


#     result=0
#     def in_a_row():
#         tmp=""
#         for s in stones:
#             tmp+=str(s)
#         return "0"*k in tmp

#     #1342104140 1
#     #0231002030 2
#     #0120001020 3
#     # tmp="1341004"
#     # if "0"*2 in tmp:
#     #     print("test")

#     while True:
#         stones=[i-1 if i>0 else 0 for i in stones]
#         result+=1
#         # print(stones)
#         # if "0"*k in stones:
#         #     break
#         if in_a_row():
#             # print("True")
#             break
