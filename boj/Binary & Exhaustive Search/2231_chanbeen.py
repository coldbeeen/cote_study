import sys

input = sys.stdin.readline

N = int(input())

result = 0

for i in range(1, N + 1):
    tmp = list(map(int, str(i).rstrip())) #분해
    
    if i + sum(tmp) == N:
        result = i
        break

print(result) if result != 0 else print(0)

#브루트포스 알고리즘 : 
#검색 대상이 되는 원본 문자열의 처음부터 끝까지 차례대로 순회하며 문자들을 일일이 비교하는 방식의 알고리즘

#O(n)으로 풀 수 있는 방법은 없었을까?