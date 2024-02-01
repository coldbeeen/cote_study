#입력 10^5 이기에 이중반복? x
#30의 배수가 되려면 3의 배수 + 10의 배수
#각 자리수 다 더해서 3이랑 10으로 나눴을 때 나오게? 는 좀 긴데

n = list(map(str, input())) #문자열로 다 나눠서 받아주고
n.sort(reverse = True) #정렬

max = "" #다루기 쉽게 문자열로

for i in range(len(n)): #제일 크게 만들어줌
    max += n[i]
 
max = int(max) #숫자형으로 바꿔주고

if max%10 != 0 or max%3 != 0:
    print(-1) #30 배수 안나오면 -1 출력

else:
    print(max) #30 배수면 temp 출력

#근데 이거 걍 n으로 쭉 가면 왜 안되는거지?
'''
n = list(map(str, input())) #문자열로 다 나눠서 받아주고
n.sort(reverse = True) #정렬
 
n = int(n) #숫자형으로 바꿔주고

if n%10 != 0 or n%3 != 0:
    print(-1) #30 배수 안나오면 -1 출력

else:
    print(n) #30 배수면 temp 출력
'''