n,m,k=map(int,input().split())
max=0
for i in range(0,k+1):
    girls=n-i
    boys=m-(k-i) # 인턴쉽 참여의 남녀 경우의 수

    girls//=2 #여자는 2인있어야 팀구성 가능
    
    team = girls if girls<boys else boys # 남녀가 한팀이기 때문에 적은쪽에 맞춰줘야 함

    max = team if team>max else max # 경우의 수중 가장 많은 팀을 만들 수 있을 때의 팀 수를 저장
    
print(max)
