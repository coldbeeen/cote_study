import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def make_candidate(string, idx):
    if len(string) == L:
        candidate.append(string)
        return
        
    if idx == C:
        return
    
    make_candidate(string+alphabet[idx], idx+1) #해당 인덱스의 알파벳 추가 O
    make_candidate(string, idx+1) #해당 인덱스의 알파벳 추가X

L, C = map(int, input().split())

alphabet = list(sorted(input().split())) #미리 사전순으로 정렬

candidate = []

make_candidate('', 0) #후보군 생성

result = []
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(candidate)): #후보군에 대한 필터링
    flag = 0
    count = 0
    
    for j in range(len(candidate[i])):
        if candidate[i][j] in vowels:
            flag = 1 #1개 이상의 모음이 존재하는지 
        else:
            count += 1
            
    if count >= 2 and flag == 1: #2개 이상의 자음이 존재하는지
        result.append(candidate[i])

for i in range(len(result)):
    print(result[i])

#최소 1개의 모음, 최소 2개의 자음
#암호는 정렬된 상태