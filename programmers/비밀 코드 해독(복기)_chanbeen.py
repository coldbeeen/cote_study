#약 28분 소요

def solution(n, q, ans):
    cases = []
    
    for i in range(1, n - 4 + 1):
        for j in range(i + 1, n - 3 + 1):
            for k in range(j + 1, n - 2 + 1):
                for a in range(k + 1, n - 1 + 1):
                    for b in range(a + 1, n + 1):
                        cases.append([i, j, k, a, b]) #각 경우의 수
    
    result = []
    
    for case in cases: #각 케이스에 대해서
        result_cnt = 0
        
        for i in range(len(q)): #각 q에 대해 검증
            cnt = 0
            
            for j in range(5):
                if case[j] in q[i]: #등장 순서는 다를 수 있기에 in 문법 사용
                    cnt += 1
            
            if cnt == ans[i]: #q 하나에 대해서 검증 완료
                result_cnt += 1
                
        if result_cnt == len(q): #모든 q의 ans와 같다면 가능한 정수 조합으로 검증
            result.append(case)
    
    return len(result)

#모든 케이스 만들고 적절하지 않은 케이스를 거르는 전략
#최악의 경우에도 30**5 정도라 중첩 반복문도 가능
#각 케이스는 숫자 5개, 오름차순
#1번째 숫자 : 1 ~ (n - 4)
#2번째 숫자 : (1번째 숫자 + 1) ~ (n - 3)
#3번째 숫자 : (2번째 숫자 + 1) ~ (n - 2)
#4번째 숫자 : (3번째 숫자 + 1) ~ (n - 1)
#5번째 숫자 : (4번째 숫자 + 1) ~ n