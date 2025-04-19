#약 27분 소요

import math

def solution(arrayA, arrayB):
    def find_gcd(array):
        result = array[0]
        
        for i in range(len(array)):
            result = math.gcd(result, array[i])
            
        return result
    
    def check(gcd, array):
        if gcd == 1:
            return False #최대공약수가 1이면 반대쪽 배열에서도 무조건 나눠지므로 조건 만족 x
        
        for i in range(len(array)):
            if array[i] % gcd == 0:
                return False #반대쪽 배열 내에 배수가 존재하면 조건 만족 x
            
        return True
    
    
    gcdA = find_gcd(arrayA)
    gcdB = find_gcd(arrayB) #배열 내 최대공약수 찾기
        
    aA = gcdA if check(gcdA, arrayB) else 0
    aB = gcdB if check(gcdB, arrayA) else 0 #각 배열 내 최대공약수가 타 배열 내에서 나눠지는지 확인
    
    return max(aA, aB) #둘 중 더 큰 값 반환

#철수 : arrayA, 영희 : arrayB
#조건 1 : arrayA의 모든 숫자의 약수, arrayB의 모든 숫자의 약수가 아님
#조건 2 : arrayB의 모든 숫자의 약수, arrayA의 모든 숫자의 약수가 아님
#길이 최대 50만, array 2번 탐색 -> O(n^2) 까지는 가능할 듯
#1. 철수와 영희 각각의 배열에서 최대공약수 찾기(함수 생성, 리스트 순회하면서 gcd 계속 갱신)
#2. 철수의 최대공약수를 영희 배열에서 체크
#3. 영희의 최대공약수를 철수 배열에서 체크
#4. 2, 3번 중 더 큰 수를 반환