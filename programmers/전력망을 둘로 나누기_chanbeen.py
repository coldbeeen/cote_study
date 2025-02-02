#약 27분 소요

from collections import deque

def solution(n, wires):
    def bfs(v):
        visited[v] = True
        
        queue = deque([v])
        
        cnt = 1
        
        while queue:
            node = queue.popleft()
            
            for n in graph[node]:
                if not visited[n]:
                    visited[n] = True
                    queue.append(n)
                    cnt += 1 #한 전력망 내 송전탑 개수 계산
        
        return cnt
    
    answer = 1e9
    
    for i in range(len(wires)): #전선을 끊을 수 있는 경우의 수들
        graph = [[] for _ in range(n + 1)]
        
        visited = [False] * (n + 1)
        
        new_wires = wires.copy()
        
        new_wires.pop(i) #전선 끊기
        
        for w in new_wires:
            s, e = w
        
            graph[s].append(e)
            graph[e].append(s) #양방향 그래프
        
        cnt1 = bfs(1) #첫번째 전력망
        
        for j in range(1, len(visited)):
            if not visited[j]:
                cnt2 = bfs(j) #두번째 전력망
                break
                
        answer = min(answer, abs(cnt1 - cnt2))
    
    return answer

#1차 제출
#n이 100까지이므로, 시간복잡도가 다소 높아도 괜찮음
#전력망을 둘로 나눌 수 있는 모든 경우의 수를 계산해서, 송전탑 개수의 차이가 가장 적은 케이스를 return
#하나의 트리가 입력으로 주어지므로, wires에서 인덱스 하나를 빼면 전력망이 둘로 나눠진 케이스가 됨
#wires 길이가 n - 1이므로, 각 wire는 각자 다른 송전탑을 연결함(start와 end 모두 겹치는 wire 없음)
#bfs 2번이면 모든 송전탑에 대해 탐색이 끝나므로, bfs(1)과 bfs(j)로 송전탑 개수 차이 계산
#무난히 통과됨