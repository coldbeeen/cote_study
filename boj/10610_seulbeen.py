#30의 배수에 혹시 규칙이 있나 해보다가 발견 => 1.일의자리 숫자는 0임  2. 각 자리 숫자들의 합이 3의 배수
import sys
from itertools import permutations # 순열함수 구글링 - permutation(list,몇개씩)=> ex): [1,2,3] => [(1,2,3),(1,3,2)...]꼴의 튜플 묶음로 출력
n=list(sys.stdin.readline())
n.remove("\n") # 개행문자 지우고
n.sort(reverse=True) #순열도 인덱스 순으로 되길래 내림차순 정렬(가장 큰거 찾고 반복문 나갈라고)
sum=0
for item in n:
    sum+=int(item) #자릿수 합 구함

if sum%3==0: #자릿수의 합이 3의 배수일때
    if '0' in n:#애초에 0이 없으면 30의 배수 못만듦
        for i in permutations(n, len(n)):
            if i[len(n)-1]=='0': # 내림차순 정렬 해놨으니 반복문 돌면서 일의자리 숫자가 0인게 처음 나오면 그게 가장 큰 30의 배수가 됨
                for j in i:
                    print(j,end="")
                exit()# 해당 인덱스 튜플의 원소 출력하고 나감
print("-1") #예외처리

# 와 잠만 사실 똑같은 말이긴 한데 생각해보니까 30이 3과 10의 최소공배수네  