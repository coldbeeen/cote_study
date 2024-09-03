#구글링

def solution(n, k, cmd):
    
    cur = k #현재 인덱스 관리용 변수
    
    table = { i:[i - 1, i + 1] for i in range(n)} #이전 번호, 다음 번호를 value로 저장하는 딕셔너리를 사용하여 링크드리스트와 같은 기능 구현 가능
    
    answer = ['O'] * n #초기값
    
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None] #헤드와 테일 지정
    
    stack = [] #삭제한 요소를 저장할 스택 배열
    
    for c in cmd:
        if c == 'C': #삭제
            answer[cur] = 'X'
            
            prev, next = table[cur]
            
            stack.append([prev, cur, next]) #삭제한 요소를 스택에 저장
            
            if next == None: #마지막 원소면 이전 인덱스(prev)를 cur에 저장
                cur = table[cur][0]
            else: #마지막 원소가 아니면 다음 인덱스(next)를 cur에 저장
                cur = table[cur][1]
                
            #cur 삭제 후 prev, next를 서로 연결
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
                
        elif c == 'Z' : #복구
            prev, now, next = stack.pop()
            
            answer[now] = 'O'
            
            #복구한 요소를 기존 테이블과 연결
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
        
        else: #위, 아래로 이동
            c1, c2 = c.split(' ')
            c2 = int(c2)
            
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1] #next
            else:
                for _ in range(c2):
                    cur = table[cur][0] #prev
        
    
    return ''.join(answer)

# 링크드리스트로 이동, 삭제, 복구 기능을 관리해야했던 문제
# 효율성 고려 측면에서 이동 시 O(n)의 복잡도가 필연적임에 유의해야함
# 링크드리스트를 딕셔너리로 구현하는 방법도 괜찮은 것 같다