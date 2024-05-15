import sys

input = sys.stdin.readline

N = int(input())

liquid = list(map(int, input().split()))

left = 0
right = N - 1 #초기화

result = abs(liquid[left] + liquid[right]) #초기화

left_idx = left
right_idx = right

while left < right: #등호가 있으면 안 됨, left와 right가 같아버리면 무조건 0이 나오기 때문
    mixed = liquid[left] + liquid[right]
    
    if abs(mixed) < result:
        left_idx = left
        right_idx = right
        result = abs(mixed) #최솟값 및 인덱스 갱신
    
    if mixed < 0: #음수면 -인 쪽이 더 크므로 왼쪽 인덱스를 오른쪽으로
        left += 1
    else: #양수면 +인 쪽이 더 크므로 오른쪽 인덱스를 왼쪽으로
        right -= 1

print(liquid[left_idx], liquid[right_idx])

#입력값은 정렬된 순서로 주어진다
#리스트 중 2개를 뽑아서 합산하여 0에 가장 가깝게 만드는 경우의 수를 찾아야 한다
#이진 탐색 느낌이지만, 후보를 하나씩 줄여가면서 연산한 느낌

#이렇게 짜면 시간 복잡도는 얼마 정도로 나오지?