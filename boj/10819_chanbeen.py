import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))

def function(array):
    result = 0
    
    for i in range(len(array) - 1): #마지막 인덱스까지는 안 감
        result += abs(array[i] - array[i + 1])
        
    return result

max = 0
case_list = list(permutations(array, N))

for case in case_list:
    output = function(case)
    
    if output > max:
        max = output

print(max)