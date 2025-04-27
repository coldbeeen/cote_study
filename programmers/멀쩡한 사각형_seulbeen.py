# 40분
# 규칙을 찾아서, w와 h에 따른 못쓰는 사각형의 개수를 구하자
# 규칙은 찾았는데, 왜 맞는지 모르겠음...

# 어차피 가로로 기나 세로로 기나 똑같으니 한 케이스만 생각
# (1,2)-> 두개, (2,4)는 *2
# (1,3)-> 3개   (2,6)은 *2
# (2,3)은 4개...
# (2,5)->6개
# (3,5) -> 7개..
# w+h-1?
# 그럼 (8,12) -> (2,3)의 4배

import math
def solution(w, h):
    # 총 사각형의 개수
    total = w * h

    # 정사각혁이면 대각선 사각형 개수는 한 변의 길이
    if w == h:
        return total - w
    
    #최대공약수==반복되는 횟수
    cnt = math.gcd(w, h)

    # 최대공약수로 나눠서 작은 직사각형? 의 변길이를 구함
    w_prime = w / cnt
    h_prime = h / cnt
    
    #사용하지 못하는 사각형의 규칙
    cant = w_prime + h_prime - 1
    print(cant)
    return total - (cant * cnt)
    
