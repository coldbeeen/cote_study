n = int(input())

result = 0
for i in range(1, n+1):

    if i < 100:  # 100 미만은 모두 한수
        result += 1

    else:
        digits = []
        while i > 0: # 각 자릿수 리스트로
            digits.append(i % 10)
            i //= 10

        prevDiff, j = digits[1] - digits[0], 1
        while j < len(digits)-1:
            if digits[j+1] - digits[j] != prevDiff:  # 자릿수의 차가 달라지면 한수 X
                break
            j += 1
        else:  # 한수 O
            result += 1

print(result)

