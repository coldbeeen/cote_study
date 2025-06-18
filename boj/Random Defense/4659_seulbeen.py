# 비밀번호 발음하기
# 23분
"""
aeiou
모음 3개 자음3개 연속 x
ee,oo제외한 같은글자 연속 x
각 조건마다 반복문을 각각 하면 시간초과가 날 것 같은데... (안났다!)
"""
import sys
input=sys.stdin.readline
# 모음 튜플
moum=('a','e','i','o','u')

#문제 조건에 맞추어 가능여부를 판단하는 함수
def check(password):
    j_cnt=0
    m_cnt=0
    m_used=0
    # 비밀번호가 한 글자일 경우 모음이기만 하면 조건 충족
    if len(password)==1:
        return True if password in moum else False

    # 반복문을 돌며 연속된 글자가 2번 왔는지, 모음이 사용되었는지 를 체크
    if password[0] in moum:
        m_used+=1
    for i in range(1,len(password)):
        if password[i] in moum:
            m_used+=1

        if password[i - 1] == password[i]:
            if password[i] != "e" and password[i] != "o":
                return False

    if m_used==0:
        return False
    
    # 자음 3연속, 모음 3연속 조건 체크
    for i in range(len(password)):
        if password[i] in moum:
            m_cnt+=1
            j_cnt=0
        else:
            m_cnt=0
            j_cnt+=1
        if j_cnt>=3 or m_cnt>=3:
            return False

    return True

while True:

    pw=input().rstrip()
    if pw=="end":
        exit()
    if check(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
