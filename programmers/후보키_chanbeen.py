from itertools import combinations

def solution(relation):
    answer = 0
    
    row = len(relation)
    col = len(relation[0])
    
    comb = []
    
    for i in range(1, col + 1):
        comb.extend(combinations(range(col), i)) #조합 가능한 열의 경우의 수 리스트에 추가
    
    unique = []
    
    for i in comb: #각 경우의 수
        tmp = []

        for item in relation: #각 행 순회
            new_tuple = ()  
            for key in i: #각 행의 열
                value = item[key] #행렬값 value로 저장
                new_tuple += (value,)
            tmp.append(new_tuple)  # 완성된 튜플을 tmp 리스트에 추가
            
        if len(set(tmp)) == row: #값 중복제거해도 행 개수와 같다? 유일성 O
            unique.append(i)
    
    answer = set(unique)
    
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])): #부분 집합이 존재하면 최소성 충족 못 함
                answer.discard(unique[j]) #삭제
    
    return len(answer)