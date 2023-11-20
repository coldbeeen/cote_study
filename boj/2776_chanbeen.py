import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    
    M = int(input())
    note2 = list(map(int, input().split()))
    
    num1_dict = {} #딕셔너리 활용하면 속도가 더 빨라짐
    
    for num1 in note1:
        num1_dict[num1] = 0 #key의 존재 유무를 확인할 것이니 value는 아무렇게 초기화
    
    for num2 in note2:
        if num2 in num1_dict:
            print(1)
        else:
            print(0)