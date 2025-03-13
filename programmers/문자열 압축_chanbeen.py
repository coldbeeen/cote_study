#약 58분 소요

def solution(s):
    def make_string(string, idx):
        if same_elem_cnt > 1 : #같은 문자가 존재할 경우
            string += str(same_elem_cnt) #숫자 추가하여 압축했음을 표시
                
        string += cut_string[idx] #문자열 붙이기
        
        return string
    
    cases = []
    
    for i in range(1, len(s) + 1): #1개 단위부터 len(s)개 단위까지 잘라서 압축해보기 위한 반복문
        cut_string = []
        compressed = ''
        
        for j in range(0, len(s), i): #i단위로 문자열 자르고, 결과물을 배열에 저장
            cut_string.append(s[j:j + i])
            
        if len(cut_string) == 1: #i == len(s)일 경우 cut_string 길이는 1, 따로 압축 진행 필요 x
            cases.append(cut_string[0])
            continue
            
        same_elem_cnt = 1 #같은 문자열이 연속으로 등장한 경우를 관리하기 위한 변수
        
        for j in range(1, len(cut_string)):
            if cut_string[j] == cut_string[j - 1]: #같은 문자열이 연속으로 등장
                same_elem_cnt += 1
            else: #다른 문자열이 등장
                compressed = make_string(compressed, j - 1) #압축 문자열에 결과 반영
                
                same_elem_cnt = 1 #변수 초기화
                
            if j == len(cut_string) - 1: #마지막 원소도 압축 문자열에 결과 반영
                compressed = make_string(compressed, j)
        
        cases.append(compressed) #i개 단위로 자른 후 압축한 문자열이 담기는 배열
    
    answer = len(cases[0])
    
    for i in range(1, len(cases)): #그 중 가장 짧은 길이를 반환
        answer = min(answer, len(cases[i]))
        
    return answer

#s 길이는 최대 1000, O(n^3)까진 괜찮을 듯
#일치하는 문자의 수가 가장 많은 문자열로 압축해야 가장 짧아짐
#문자열은 가장 앞부터 정해진 길이만큼 자름 (입출력 예시 5), 유의
#자를 수 있는 모든 경우의 수를 리스트에 담고, 가장 길이가 짧은 예시를 반환하는 형식으로 시도
#반복문을 통해서 n개 단위로 자르는 경우를 테스트
#테스트 케이스 5번이 틀렸으나 i가 len(s)일 때 cut_string 배열 길이가 1이므로 이 경우에 대한 예외 처리를 진행했더니 통과