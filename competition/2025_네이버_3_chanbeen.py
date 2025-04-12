import sys

from itertools import combinations

input = sys.stdin.readline

N = int(input())
fruits = list([input().rstrip() for _ in range(N)])

k = int(input())
cases = list(combinations(fruits, k))

fruit_dict = {}

for case in cases:
    flavor = ['0'] * len(fruits[0])
    
    for c in case:
        for i in range(len(c)):
            if c[i] == '1':
                flavor[i] = '1'

    mixed = ''.join(flavor)
    
    if mixed in fruit_dict:
        fruit_dict[mixed] += 1
    else:
        fruit_dict[mixed] = 1
        
print(fruit_dict)
print(len(fruit_dict.keys()))

#완전탐색이 아닌 방법이 생각나지 않는다.. 

#입력예시
# 4
# 1100
# 0110
# 0011
# 1100
# 2

# 6
# 100
# 100
# 011
# 100
# 111
# 011
# 1

# 6
# 100
# 100
# 011
# 100
# 111
# 011
# 5

# 9
# 001
# 001
# 001
# 010
# 010
# 010
# 010
# 100
# 100
# 3