#구글링
import sys

input = sys.stdin.readline

N = int(input())

operand = list(map(int, input().split())) # 피연산자

operator = list(map(int, input().split())) # +, -, x, //

def backtrack(idx, result):
    global max_num, min_num
    
    if idx == N: #N개의 수에 대한 연산이 끝나면 비교 후 반환
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    
    if operator[0] > 0: #덧셈
        operator[0] -= 1
        backtrack(idx + 1, result + operand[idx])
        operator[0] += 1 
        #연산이 끝난 후에는 다시 복구해줘야 모든 경우에 대한 탐색이 가능함
    
    if operator[1] > 0: #뺄셈
        operator[1] -= 1
        backtrack(idx + 1, result - operand[idx])
        operator[1] += 1
        
    if operator[2] > 0: #곱셈
        operator[2] -= 1
        backtrack(idx + 1, result * operand[idx])
        operator[2] += 1
        
    if operator[3] > 0: #나눗셈
        operator[3] -= 1
        backtrack(idx + 1, int(result / operand[idx]))
        #result // operand[idx]로 하면 틀림
        #int(result / operand[idx]) 꼴이 음수 나눗셈도 제대로 계산하는 듯
        operator[3] += 1
        
max_num = -1000000000 #교체를 위한 최댓값
min_num = 1000000000 #교체를 위한 최솟값

backtrack(1, operand[0])

print(max_num)
print(min_num)

#결국에는 베이스케이스 + 반복문(선택) + 조건문 + 조건문 충족 시 리스트의 다음 인덱스 & 재귀 호출의 구조구나