#60분 +@, 구글링

import math

def solution(w,h):
    
    return w * h - (w + h - math.gcd(w, h))

#W, H가 입력 범위가 각각 1억
#1중 반복문에서 끝내야 함

#1차 제출
#한 열에서 사용할 수 없는 사각형 개수 k를 계산하면, k * W를 수행하여 사용할 수 있을 것 같다
#예시를 봤을 때 k가 모든 열에서 동일해보이기 때문
#W와 H의 비율을 보면, 예시에서 2:3이고 가로 길이가 1일 때 세로 길이는 1.5이다
#H에서 H/W를 빼준 뒤 남은 소수점은 버림해주면 한 열당 사용할 수 있는 정사각형 개수 k 구하기 가능
#50점..
#모든 열이 같은 개수를 사용하지 못 하는 것은 아닌가봄 (w, h가 홀수와 짝수일 때 등)

#구글링
#예시 그림에서, 비어있는 사각형을 위와 왼쪽으로 밀어붙여보면 규칙이 보인다
#(W + H)개 중에서 몇 개는 채워져있는 걸 확인할 수 있는데, 그것은 W와 H의 최대공약수이다
#따라서, 답 = H * W - (W + H - 최대공약수(W, H))
#역시 규칙이 존재했던 것 맞았으나, 이런건 어떻게 생각해내는지 벽을 다시 한번 느낌