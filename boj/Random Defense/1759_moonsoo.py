import sys

global N, L, C

def DFS(index, depth):

    stack.append(alphabet[index])

    if depth == L:
        # L개의 문자가 스택에 모였을 때
        intersection = set(stack) & set(vowels)
        complement = set(stack) - set(vowels)
        if (len(intersection) >= 1) and (len(complement) >= 2):
            # 종료조건: 최소 한 개의 모음과 두 개의 자음이 남아있지 않으면 종료
            print(intersection, complement)
            # 가능성 있는 암호 출력
            print(''.join(stack))
        # top원소를 지워주어 다른 원소가 올 수 있도록 한다.
        stack.pop()

        # 종료조건: L시점에서 종료해주어 불필요하게 그 이상의 원소를 탐색하지 않는다.
        return

    for i in range(index + 1, N):
        # 다음 경우의 수를 확인하러 넘어간다
        DFS(i, depth + 1)
    
    # 같은 레벨에서의 서치가 다 끝난 경우, 이전 레벨의 다음 원소를 확인하기 위해 pop을 한 번 더 해준다.
    stack.pop()


L, C = map(int, input().split())
alphabet = list(map(str, input().split()))

# 알파벳 증가하는 순서 출력 위해 정렬
alphabet.sort()

stack = []
vowels = ['a', 'e', 'i', 'o', 'u']

N = len(alphabet)

for i in range(C - L + 1):
    # 모든 알파벳을 시작 지점으로 탐색. L개를 만들지 못하는 경우는 탐색x
    DFS(i, 1)

