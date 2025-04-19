# 42분
# 찬빈이가 알려준 gcd
import math

def solution(arrayA, arrayB):
    a, b = 0, 0

    #배열 A,B에 대한 최대공약수 
    for i in range(len(arrayA)):
        a = math.gcd(a, arrayA[i])
    for i in range(len(arrayB)):
        b = math.gcd(b, arrayB[i])

    # 각 배열의 최대공약수를 각각 구했으니, 다른 배열의 최대공약수로는 나눠지면 안됨(나눠지면 조건에 어긋나는 것임!)
    for i in range(len(arrayA)):
        
        if arrayA[i] % b == 0:
            b = 1
        if arrayB[i] % a == 0:
            a = 1

    #둘다 조건에 어긋났던 상태라면 return 0
    if a == 1 and b == 1:
        return 0
    # 조건을 만족하는 수 중 가장 큰 값 return
    return max(a, b)
