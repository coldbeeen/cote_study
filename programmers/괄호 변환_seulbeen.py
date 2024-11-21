# 40분
# 뇌빼고 시키는대로 구현만했는데도 40분걸리네
def solution(p):
    #리스트로 변환
    p = list(p)

    #올바른 괄호인지 체크하는 함수
    def olbarun(gwalho):
        stack = []
        for g in gwalho:

            #열린괄호일 때는 stack에 추가
            if g == "(":
                stack.append(g)
            
            #닫힌 괄호일 때
            else:
                #닫힌괄호가 존재하는데 열린괄호가 남아있을 시 False
                if not stack:
                    return False
                
                #현재 닫힌괄호는 열린괄호중 가장 나중에 들어온애랑 짝지어지므로 pop
                stack.pop()

        #반복문을 완료하였는데도 열린괄호가 남아있다면 False
        if stack:
            return False
        return True

    #균형잡힌 괄호인지 확인
    def balance(gwalho):
        cnt_left = 0
        cnt_right = 0

        #단순히 열린괄호와 닫힌괄호의 수를 비교해서 비교후 return 
        for g in gwalho:
            if g == "(":
                cnt_left += 1
            else:
                cnt_right += 1
        return cnt_left == cnt_right
    
    # 문자열을 u와 v로 나누는 함수
    def split(gwalho):
        u = []
        for i in range(len(gwalho)):
            # u에 괄호를 하나씩 append
            u.append(gwalho[i])

            # u가 균형잡힌 괄호 문자열이라면 u와 그 나머지(v)를 반환
            if balance(u):
                return u, gwalho[i + 1 :]
    #문제에서 시키는대로 하는 함수
    def recurse(gwalho):
        # 빈 문자열일시 그대로 빈 문자열 반환
        if not gwalho:
            return []
        
        # u,v로 분할
        u, v = split(gwalho)
        
        # u가 올바른 괄호 문자열일 때, v를 처음부터 재귀적으로 시행한 후 u에 이어붙이고 반환
        if olbarun(u):
            tmp = recurse(v)
            u.extend(tmp)
            return u
        
        # 올바르지 않다면
        else:
            #빈 문자열에 ( 를 붙임
            empty = ["("]
            
            # v에 대해 재귀적으로 수행한 결과를 이어붙임
            tmp = recurse(v)
            empty.extend(tmp)

            # ) 를 다시 붙임
            empty.append(")")

            # u의 양 끝 문자를 제거하고 나머지 문자의 괄호방향을 뒤집어서 이어붙임
            u = u[1 : len(u) - 1]
            for g in u:
                if g == "(":
                    empty.append(")")
                else:
                    empty.append("(")
            # 결과 반환
            return empty

    answer = recurse(p)

    #결과의 리스트의 괄호들을 str로 만들어줌
    answer = "".join(answer)
    return answer
