# 너의 평점은
# 9분
"""
시키는 대로 하면 되는 문제
각 평점에 따른 점수를 딕셔너리로 만들었고, 학점 * 평점을 해서 모두 더한 뒤 전체 수강 학점으로 나눴음
"""
import sys

input=sys.stdin.readline
total_score=0.0
total_hak=0.0
hak_dict={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
for _ in range(20):
    sub,hak,score=input().split()
    hak=float(hak)
    if score=='P':
        continue
    total_hak+=hak
    total_score+=hak_dict[score]*hak
result=total_score/total_hak
print(result)    
