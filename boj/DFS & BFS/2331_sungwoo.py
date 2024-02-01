a, p = map(int, input().split())

def d(n, p):  # n과 p를 사용해 다 수열값 계산
    result = 0
    while n > 0:  # 자릿수 순회
        result += (n % 10) ** p
        n //= 10

    return result

l = []
val = a
while True:
    l.append(val)  # 처음 수열값부터 시작해 리스트에 추가
    val = d(val, p)  # 다음 수열값 계산

    if val in l:  # 이미 나왔던 수열값이라면
        print(l.index(val))  # 해당 값 인덱스 출력 후 반복문 종료
        break