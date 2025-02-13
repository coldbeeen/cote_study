#약 29분 소요

from collections import deque

def solution(begin, target, words):
    def BFS(begin, target, words):
        queue = deque([[begin, 0]])
        
        while queue:
            popped, stage = queue.popleft()
            
            if popped == target:
                return stage
            
            for w in words: #단어별
                cnt = 0
                
                for i in range(len(popped)):
                    if w[i] != popped[i]: #pop된 단어와 다른 알파벳 개수 카운트
                        cnt += 1
                
                if cnt == 1: #알파벳 1개만 다르면 변환 가능, 큐에 삽입
                    queue.append([w, stage + 1])
        
        return 0 #변환 실패
    
    if target not in words:
        return 0
    
    return BFS(begin, target, words)

#최소 단계 -> bfs
#begin은 words내에 존재 x -> visited 사용이 애매해짐
#target이 words 안에 없다면 변환이 불가능함 -> 0 반환
#한번에 하나의 알파벳만 변환 가능
#pop된 단어와 words의 단어들을 비교, 다른 알파벳 개수가 1개인 단어만 큐에 삽입
#제출하니 바로 통과

#visited가 없어서 한번 방문한 단어가 다시 큐에 담기는 현상이 있는데, 어떻게 해결해야할지..?