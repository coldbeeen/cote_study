import sys

input = sys.stdin.readline
paper = ''

T = int(input())

def check_paper(paper):
    if len(paper) == 1: #1번만 접었거나, 끝까지 대칭 원소간 비대칭을 유지하는 경우(끝까지 접을 수 있는 경우)
        return True
    
    for i in range(len(paper) // 2):
        if paper[i] == paper[-1 - i]: #대칭 원소끼리 비교하면서, 한번이라도 대칭이 발생하면
            return False #동호의 규칙대로 종이를 접을 수 없다
    
    return check_paper(paper[:len(paper)//2]) and check_paper(paper[len(paper)//2 + 1:]) #재귀 함수 구조로 원래 접힌 형태에서 앞 절반과 뒤 절반을 계속 확인

for _ in range(T):
    paper = input().rstrip()
    
    if check_paper(paper):
        print("YES")
    else:
        print("NO")