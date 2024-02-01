import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    num1 = set(map(int, input().split()))
    m = int(input())
    num2 = list(map(int,input().split()))

    for num in num2:
        print(1 if num in num1 else 0) # 아래꺼보다 이게 더 간지남

'''
    for num in num2:
        if num in num1:
            print(1)
        else:
            print(0)
'''