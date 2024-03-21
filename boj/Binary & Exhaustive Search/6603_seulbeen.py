#순열 쓰면 안되나...?
from itertools import permutations
import sys
input=sys.stdin.readline

while True:
    lotto=list(map(int,input().split())) 
    if lotto[0]==0:
        break
    
    cases=permutations(lotto[1:],6) #순열로 경우의 수 구함

    for each_case in cases: 
        flag=1
        for i in range(len(each_case)-1): # 각각의 경우에 오름차순으로 정렬된 경우만 출력
            if each_case[i]>each_case[i+1]:
                flag=0
                break
        if flag==1:    
            print(*each_case)
    print("")    
    
