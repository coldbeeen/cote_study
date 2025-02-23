#약 30분 소요

def solution(n, q, ans):
    def make_cases():
        for a in range(1, n + 1 - 4): #첫째 자리에 n - 4까지 올 수 있음
            for b in range(a + 1, n + 1 - 3): #둘째 자리에 n - 3까지 올 수 있음
                for c in range(b + 1, n + 1 - 2): #셋째 자리에 n - 2까지 올 수 있음
                    for d in range(c + 1, n + 1 - 1): # ...
                        for e in range(d + 1, n + 1): # ...
                            array = [a, b, c, d, e]
                            cases.append(array)
    
    cases = []
    
    make_cases()
    
    result = []
    
    for case in cases:
        ans_cnt = 0
        
        for i in range(len(q)):
            cnt = 0
            
            for j in range(len(case)):
                if case[j] in q[i]:
                    cnt += 1
                    
            if cnt == ans[i]: #case와 q[i]의 교집합 내 원소 개수가 ans[i]와 같다
                ans_cnt += 1 #q[i]에 대해서는 case가 조건을 만족
        
        if ans_cnt == len(q): #case가 q 내 모든 케이스에 대해서 조건을 만족하면
            result.append(case) #이 case는 비밀 코드 후보가 될 수 있음
    
    return len(result)

#비밀 코드 : 1 ~ n 중 5개 정수, 오름차순 정렬
#비밀 코드로 조합 가능한 경우의 수를 만들고, m번의 테스트를 통해서 ans와 같지 않으면 필터링하는 방식
#5번의 재귀 함수 호출을 통해서, 가능한 경우의 수 만들기
#경우의 수 조합에 5중 반복문, 필터링 단계에서 4중 반복문을 사용
#조합 가능한 경우의 수는 최대가 n이 30일 때, 넉넉하게 잡아도 30^5
#q의 최대 길이는 10, q[i]의 길이는 5 여서 빡센 범위 제한 덕분에 무사히 통과