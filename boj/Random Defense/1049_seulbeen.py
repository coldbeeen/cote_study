# 기타줄
# 


"""
n개의 기타줄을 고치는데, 6개 패키지로 사는게 나을지 or 낱개로 사는 것이 나을지?

가능한 경우의 수는 3가지
1. 싹다 낱개로 사기
2. 패키지로 살 수 있는 만큼 사고, 나머지를 낱개로 사기
3. 혹은, 줄이 남더라도 패키지 가격으로 한묶음 남게 더 사기

또한, 꼭 같은 브랜드의 기타줄을 살 필요는 없음
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

guitars=[list(map(int,input().split())) for _ in range(m)]

# 낱개가격을 담은 리스트, 묶음 가격을 담은 리스트, 이때 묶음 가격을 담은 리스트에는 낱개로 6개를 사는 경우도 포함
single_price=[x[1] for x in guitars]
package_price=[]
for g in guitars:
    p,s=g[0],g[1]
    package_price.append(g[0])
    package_price.append(g[1]*6)

# 패키지 가격과 낱개가격의 최솟값
min_package=min(package_price)
min_single=min(single_price)

# 낱개로 전부 구매
total=[min_single*n]

# 패키지로 한묶음 더 남게 구매
total.append(min_package*((n//6)+1))

# 개수 맞춰서 패키지와 낱개 혼합
total_tmp=0
total_tmp+= min_package*(n//6)
n%=6
total_tmp+=min_single*n
total.append(total_tmp)

#세 경우의 수중 최솟값 반환
print(min(total))
