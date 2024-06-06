import sys

input = sys.stdin.readline

n = int(input())
num_list = sorted(list(map(int, input().split())))
x = int(input())

left = 0
right = n - 1 #인덱스

cnt = 0

while left < right:
    if num_list[left] + num_list[right] == x:
        cnt += 1
        left += 1 #right를 한 칸 왼쪽으로 해도 괜찮을 듯
    elif num_list[left] + num_list[right] > x:
        right -= 1
    else:
        left += 1
        
print(cnt)

#이진 탐색과 유사한 문제(투 포인터)
#i와 j를 각각 left와 right로 설정
#조건에서 i와 j에 등호가 없으므로, left와 right가 만나면 안 됨