n = int(input())

i, nthNum = 0, 0
while nthNum < n:  # n번째 종말 수까지 순회
    if '666' in str(i):  # 666 포함된 수라면 nthNum 1 증가
        nthNum += 1
    i += 1

print(i-1)  # 마지막에 더해진 1 감소 후 출력