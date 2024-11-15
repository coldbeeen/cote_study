# 18:57- 19:24 (27분)
# 일단 한행에 무조건 하나씩 넣고
# 열이 같으면 안됨(같은 원소가 있으면 안됨)
# 대각선상에 있으면 안됨(행번호 차이랑 원소 차이랑 같으면 안됨)
# [0,1,2,3]
"""
19시 45분
비상상황 :  주석 달아놓고 다시 돌렸는데 마지막 테스트케이스 갑자기 시간초과 뜸
주석지워봐도 시간초과뜨고  맞았던 코드 그대로 넣어도 시간초과뜸 뭐지? 뽀록으로 정답이 뜬건가?
"""


def solution(n):

    global answer
    answer = 0
    chess = [0 for _ in range(n)]
    visit = [False for _ in range(n)]

    def check(idx):
        # ex: idx행을 검사할 예정
        # chess[idx](idx행의 열 번호)!=chess[i] 윗 행들의 같은 열에 없어야 함
        # 행 차이가 열차이랑 같으면 대각선에 있다는 뜻=> (1,1),(2,2)(3,3) or (1,2) (2,3)
        for i in range(idx):
            if chess[i] == chess[idx] or idx - i == abs(chess[idx] - chess[i]):
                return False
        return True

    def backtracking(idx):
        global answer

        if idx == n:
            answer += 1
            return
        for i in range(n):
            # 방문하지 않은 행이라면
            if visit[idx] == False:
                # 그 행에다가 하나씩 퀸을 놔봄
                chess[idx] = i

                # 유효한 자리라면
                if check(idx):
                    # 백트래킹
                    visit[idx] = True
                    backtracking(idx + 1)
                    visit[idx] = False

    backtracking(0)

    return answer
