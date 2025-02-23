# 30분
from collections import deque
def solution(begin, target, words):
    
    #target이 단어모음에 없으면 못바꿈
    if target not in words:
        return 0
    # 한글자만 바꿀 수 있다는 규칙을 위배 하는지(단어를 바꿀 수 있는지)
    def change(cur, tar):
        dif = 0
        for c, t in zip(cur, tar):
            if c != t:
                dif += 1
            #두 글자 이상 차이 난다면 못바꿈
            if dif > 1:
                return False
        return True

    #BFS
    q = deque()
    q.append((begin, 0))
    while q:
        #(현재 단어와, 바꾼 횟수)
        word, cnt = q.popleft()
        
        # 타겟 단어랑 일치하면 cnt return
        if word == target:
            return cnt
        # 단어 모음에서 변환 가능한 단어로 변환해서 BFS 시행
        for change_word in words:
            if change(word, change_word):
                q.append((change_word, cnt + 1))
