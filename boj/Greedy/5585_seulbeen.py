n=int(input())
tmp=1000-n
cnt=0

while(tmp>0):
    if(tmp>=500):
        tmp-=500
        cnt+=1
    elif(tmp>=100):
        tmp-=100
        cnt+=1
    elif(tmp>=50):
        tmp-=50
        cnt+=1

    elif(tmp>=10):
        tmp-=10
        cnt+=1
        
    elif(tmp>=5):
        tmp-=5
        cnt+=1
    else:
        tmp-=1
        cnt+=1
print(cnt)
    
