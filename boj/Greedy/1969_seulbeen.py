#a.index() 메소드 구글링
# 줇바꿈 없이 출력하는 법 구글링 ㅋㅋ
n,m=map(int,input().split())
mini=0
cnt=0
list=[] # 처음 입력
dna=['A','C','G','T'] # 서열 정보 저장
result=[]# 결과 출력할 리스트

for i in range(n):
    list.append(input())

for j in range(m):
    dnacnt=[0,0,0,0]
    for i in range(n):
        if list[i][j]==dna[0]:
            dnacnt[0]+=1
        elif list[i][j]==dna[1]:
            dnacnt[1]+=1
        elif list[i][j]==dna[2]:
            dnacnt[2]+=1
        else:
            dnacnt[3]+=1
    cnt+=max(dnacnt) #최빈문자 +
    idx=dnacnt.index(max(dnacnt)) #가장 많이 등장했던 횟수의 인덱스를 찾음, 즉 hamming distance가 가장 적을 문자의 인덱스 알기 위함
    result.append(dna[idx]) # 그 인덱스에 해당하는 문자 result에 추가

min_ham_dis=n*m-cnt # 해밍턴거리의 '최소' => 각 열에서 최빈문자가 아닌 글자들의 개수(최빈문자들로만 이루어져야 최솟값이 나오기 때문) 
for item in result:
    print(item,end="")

print("\n%d"%min_ham_dis)
