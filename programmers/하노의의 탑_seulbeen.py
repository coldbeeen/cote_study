# 65분 후 풀이 참조,,, 로직은 알았는데 구현을 못했음
# 현타오네...
# n-1개의 원판을 나머지에 옮겨놓고, 맨 밑에 가장 큰 원판 하나를 목표원판에 옮긴다
def solution(n):
    answer = []

    def hanoi(start, end, tmp, N):
        if N == 1:
            return [[start, end]]
        # for i in range(N-1):
        #     answer.append([start,tmp])
        # answer.append([start,end])
        # return hanoi(tmp,end,start,N-1)

        print(f"{start},{end}")
        return (
            hanoi(start, tmp, end, N - 1)
            + [[start, end]]
            + hanoi(tmp, end, start, N - 1)
        )

    answer = hanoi(1, 3, 2, n)
    return answer
