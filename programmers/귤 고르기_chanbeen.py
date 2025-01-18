#약 40분 소요

def solution(k, tangerine):
    answer = 0
    
    gyul = {}
    
    for i in tangerine: #크기별 개수 세는 딕셔너리로 변경
        if i in gyul:
            gyul[i] += 1
        else:
            gyul[i] = 1
            
    sorted_gyul = sorted(gyul.items(), reverse = True, key = lambda x : x[1]) #개수 기준 내림차순 정렬
    
    for g in sorted_gyul: #개수 큰 것 부터 순회
        if k <= 0: #k개 충족했음
            return answer 
        
        k -= g[1]
        answer += 1 #종류 + 1
                    
    return answer #k = len(set(tangerine))

#1차 제출
#combinations로 경우의 수 만들어서 set로 만든 뒤 가장 짧은 len을 반환하면 될 줄 알았으나 시간 초과 발생
#모든 케이스에 대해 set으로 만들어버리니 시간이 많이 소요되는 듯

#2차 제출
#combinations 사용하지 않기로 결정
#크기별 개수를 센 뒤, 개수가 가장 많은 크기부터 종류 개수를 카운트해주면 될 듯
#이를 위해 tangerine을 딕셔너리 형태로 변경
#딕셔너리를 내림차순으로 정렬하고, 개수 많은 key부터 순회하며 종류 개수 answer로 카운트
#k - gyul[i] 해가면서 0보다 작아지면 answer 반환