result=[]
while True:
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        break #종료조건
    seq=0# 연속으로 며칠?
    share=v//p # 전체 휴가를 연속된 일수로 구간 나눔
    seq+=share*l # 각 구간당 최대 가용일수 * 구간 수
    remain=v%p # 구간으로 나누고 나머지 휴가 수


    if remain>l:
        seq+=l # 남은 일수가 가용일수보다 넉넉하면 그냥 가용일수 ㄱㄱ
    else:
        seq+=remain # 아니면 남은 일수 ㄱㄱ
    result.append(seq)
for i in range(len(result)):
    print("Case %d: %d"%(i+1,result[i]))    
