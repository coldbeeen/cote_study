import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    num = list(map(int, input().split()))
    
    k = num[0]
    c = num[1:]
    
    if num[0] == 0:
        break
    
    case_list = list(combinations(c, 6)) 
    #무조건 오름차순으로 주어지니까 순서 필요없는 조합으로 구하면 다 구해짐
    
    for case in case_list:
        print(*case) # * 구글링 -> 그새 까먹었네, 근데 한 칸 띄고 출력이 디폴트였나? 
        
    print()
    
    #백트래킹으로 푸는걸 연습해야됨