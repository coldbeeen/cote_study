import sys

input = sys.stdin.readline

N = int(input())
operand = list(map(int, input().split()))
operator = list(map(int, input().split())) # +, -, *, /

def calculate(idx, num):
    global max_num, min_num
    
    if idx == N:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        
        return
    
    if operator[0] > 0:
        operator[0] -= 1
        calculate(idx + 1, num + operand[idx])
        operator[0] += 1
    
    if operator[1] > 0:
        operator[1] -= 1
        calculate(idx + 1, num - operand[idx])
        operator[1] += 1
        
    if operator[2] > 0:
        operator[2] -= 1
        calculate(idx + 1, num * operand[idx])
        operator[2] += 1
        
    if operator[3] > 0:
        operator[3] -= 1
        calculate(idx + 1, int(num / operand[idx]))
        operator[3] += 1

max_num = float("-inf")
min_num = float("inf")

calculate(1, operand[0])

print(max_num)
print(min_num)

#연산자 끼워넣기(2)랑 다른 부분이 뭐지?