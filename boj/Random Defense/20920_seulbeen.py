#영단어 암기는 괴로워
#7분
"""
시키는대로 하면 되는 문제인듯
"""
import sys
from collections import defaultdict,Counter
input=sys.stdin.readline
words=[]
N,M=map(int,input().split(" "))

for _ in range(N):
    word=input().rstrip()
    # 단어의 길이가 M 이상일 때만 단어장으로 만듦
    if len(word)>=M:
        words.append(word)
# 각 단어별 등장 횟수를 Counter로 셈
# Key : 단어 / Value : 등장 횟수   
c=Counter(words)
"""
 문제의 조건에 맞게 정렬
 1.등장 횟수
 2.단어의 길이
 3.단어의 알파벳순
"""
result=sorted(c.items(),key=lambda x: (-x[1],-len(x[0]),x[0]))
for r in result:
    print(r[0])