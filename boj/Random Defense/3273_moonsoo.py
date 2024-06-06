import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

cnt = 0
l, r = 0, len(arr) - 1
while l < r:
    current_sum = arr[l] + arr[r]
    if current_sum >= x:
        if current_sum == x:
            cnt += 1
        r -= 1
    else:
        l += 1

print(cnt)

"""
문제:
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열과 자연수 x가 주어질 때, 두 수의 합으로 x를 만들 수 있는 경우의 수 구하기
(1 <= i < j <= n)
----------------------------------------------------------------------------------------------------------------------------
풀이:
주어진 배열은 서로 다른 양의 정수이므로 sort해준 후, 양 끝을 l, r 투 포인터를 잡는다.
이후 arr배열의 l과 r번째 위치의 합을 구한 후, x와 비교하며 l, r을 움직이며 카운팅한다.
"""