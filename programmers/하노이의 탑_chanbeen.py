#45분 소요, 이후 구글링
#로직은 이해했으나 재귀 코드로 구현을 못 하겠음

def solution(n):
    def hanoi(source, target, intersection, n):
        if n == 1:
            answer.append([source, target])
        else:
            hanoi(source, intersection, target, n - 1) #n-1개 출발 -> 중간
            hanoi(source, target, intersection, 1) #출발 -> 도착
            hanoi(intersection, target, source, n - 1) #n-1개 중간 -> 도착
    
    answer = []
    
    hanoi(1, 3, 2, n)
    
    return answer

#내가 생각했던 로직
#n-1개를 1번 또는 2번 기둥에 다 옮기고, n번째를 3번으로 옮긴다
#n을 1 줄이고, n이 1이 될 때까지 위 과정을 다시 반복한다

#일반화(구글링)
#처음 원판이 있는 기둥 : 출발, 3번 기둥 : 도착, 나머지 기둥 : 중간
#n-1개를 중간 기둥으로 옮긴다(재귀)
#n번째를 도착 기둥으로 옮긴다
#n-1개를 도착 기둥으로 옮긴다(재귀)