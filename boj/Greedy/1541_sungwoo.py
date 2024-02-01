import sys, re
input = sys.stdin.readline

expr = input().rstrip()
numbers = re.split(r'[+-]', expr)
operators = re.split(r'\d+', expr)[1:-1]  # split 수행 시 양 끝은 빈 문자열

# - 연산자가 하나라도 있다면, 해당 위치부터 맨 뒤까지 모든 수를 빼주면 원하는 결과가 나옴
minusIdx = operators.index('-') if '-' in operators else len(operators)
result = sum(map(int, numbers[:minusIdx+1])) - sum(map(int, numbers[minusIdx+1:]))
print(result)