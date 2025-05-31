#약 12분 소요

def solution(n):
    def hanoi(start, end, via, n):
        if n == 1:
            answer.append([start, end])
            
            return
        
        hanoi(start, via, end, n - 1)
        hanoi(start, end, via, 1)
        hanoi(via, end, start, n - 1)
        
    answer = []
    
    hanoi(1, 3, 2, n)
    
    return answer

#1 2 3 기둥이 있을 때
#1. n - 1개의 원판을 출발(1) -> 도착(2)
#2. 가장 마지막에 남아있는 원판 1개를 출발(1) -> 도착(3)
#3. n - 1개의 원판을 출발(2) -> 도착(3)
#base case : n이 1이면, 원판을 도착 지점으로 옮기면 되므로 [출발, 도착]을 append하고 return

#하노이 탑 알고리즘은 이제 이해한 듯 함