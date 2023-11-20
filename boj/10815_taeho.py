# 구글링
# 주어진 범위가 저렇게 크면
# 이진탐색 - bisect 사용하여 구현


import bisect
N = int(input())
card = list(map(int, input().split()))
M = int(input())
other = list(map(int, input().split()))
card.sort()
answer = [0] * M

for o in other:
    l = bisect.bisect_left(card, o)
    r = bisect.bisect_right(card, o)
    print(r - l, end=' ')

'''
from bisect import bisect_left, bisect_right
n = int(input())
my_card = sorted(list(map(int, input().split())))
m = int(input())
input_card = list(map(int, input().split()))
for i in input_card:
    if bisect_left(my_card, i) == bisect_right(my_card, i):
        print(0, end=" ")
    else:
        print(1, end=" ")


# 이는 정렬된 리스트를 기반으로 수행하기 때문에 my_card는 기본적으로 오름차순 정렬을 수행해준다.
# bisect_left는 왼쪽부터 이분탐색을 통해 매개변수로 입력된 숫자가 들어갈 위치를 return해주고, 
# bisect_right는 오른쪽부터 마찬가치로 수행한다.
# 똑같은 숫자를 똑같은 리스트에서 bisect_left, bisect_rignt를 하여 이 두개가 같다면 리스트에 해당 숫자가 없다는 것이다.       
'''