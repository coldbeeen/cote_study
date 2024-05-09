# 자음 모음 조건 까먹고 있었음
import sys
from itertools import combinations

l,c=map(int,input().split())
letters=input().split()
# 조합 뽑고 정렬하려했는데 정렬이 잘 안되어서 입력과 동시에 정렬했더니 되네?
letters.sort()
moeum=['a','e','i','o','u']

candidates=list(combinations(letters,l)) # 튜플 형식이라서 리스트로 새로 만들어줌

tmp=[]
for i in candidates:
    tmp.append(list(i))

for password in tmp:
    m_cnt=0
    j_cnt=0
    for each in password: #자음 모음 조건에 맞춰서 개수 카운트
        if each in moeum:
            m_cnt+=1
        else:
            j_cnt+=1
    if m_cnt>=1 and j_cnt>=2:
        print("".join(password))
