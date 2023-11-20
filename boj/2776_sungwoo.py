import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    setOfNote1 = set(note1)  # note1을 집합 자료형(set)으로! -> 해시 기반 자료구조라 탐색 O(1)
    for numOfNote2 in note2:  # note2를 순회
        print(1 if numOfNote2 in setOfNote1 else 0)  # numOfNote2가 포함 되어 있다면 1, 아니면 0


    # O(nlogn) 왜 안될까...
    # note1.sort()
    # for numOfNote2 in note2:
    #     start, end, result = 0, n-1, 0
    #
    #     while start <= end:  # 수첩1을 대상으로 이진 탐색 수행
    #         mid = (start + end) // 2
    #
    #         if note1[mid] > numOfNote2:
    #             end = mid - 1
    #         elif note1[mid] < numOfNote2:
    #             start = mid + 1
    #         else:
    #             result = 1
    #             break
    #
    #     print(result)