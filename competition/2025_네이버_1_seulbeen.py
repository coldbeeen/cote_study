# 모든 0인 경우인 수를 세면서, 발사/안발사를 각자 세면 되지 않을까?
# 0인 인덱스를 다 찾냐 마냐 ...
import ast
def solution(cylinder,a):
    result=[]
    mo=0
    ja=0
    n=len(cylinder)
    no_bullet=list(filter(lambda x: cylinder[x]==0,range(len(cylinder))))
    for idx in no_bullet:
        cnt=0
        flag=0
        while cnt<a:
            idx=(idx+1)%n
            cnt+=1
            if cylinder[idx]==1:
                flag=1
                break
        if flag:
            mo+=1
        else:
            mo+=1
            ja+=1
    for i in range(min(mo,ja),1,-1):
        if mo%i==0 and ja%i==0:
            mo//=i
            ja//=i
            break
    result.append(ja)
    result.append(mo)



    return result

cylinder=input()
cylinder=ast.literal_eval(cylinder)
a=2
# print(cylinder[0])
output = solution(cylinder,a)
print(output)
