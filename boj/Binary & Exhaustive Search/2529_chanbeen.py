#구글링
import sys

input = sys.stdin.readline

k = int(input())

sign = list(input().split())

visited = [0] * 10 #방문여부 체크하는 배열

def check(i, j, sign): #옳은 대소관계인지 비교하는 함수
    if i < j:
        if sign == '>':
            return False
        
    if i > j :
        if sign == '<':
            return False
    
    return True #문자형이 입력되어도 파이썬에서는 사전순으로 비교하기 때문에 풀이상 오류 발생 x

def backtrack(idx, num):
    if idx == k + 1:
        answer.append(num)
        return
        
    for i in range(10): #0 ~ 9
        if not visited[i]: #아직 방문하지 않은 숫자에 대해
            if idx == 0 or check(num[idx - 1], str(i), sign[idx - 1]):
                visited[i] = 1
                backtrack(idx + 1, num + str(i))
                visited[i] = 0 #모든 경우의 수 체크를 위해 복구

answer = [] #나올 수 있는 경우의 수를 모두 저장하는 배열

backtrack(0, '') #num을 문자형으로 넣어야 이어붙이기 편함

answer.sort() #역시 문자형이지만 사전순으로 비교하여 정렬하기 때문에 풀이상 오류 발생 x

print(answer[-1]) #최댓값
print(answer[0]) #최솟값

#15658번과 유사한 느낌