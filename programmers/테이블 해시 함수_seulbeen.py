# 35분
# 비트와이즈 XOR이 뭔가 했는데 연산자가 있었음 -> a^b
def solution(data, col, row_begin, row_end):
    answer = 0
    xor = []

    #S_i 계산 함수
    def si(idx):
        result = 0
        # 문제에서 i번째 컬럼은 리스트상으로 i-1번째 컬럼인 것에 유의
        for num in data[idx - 1]:
            result += num % idx
        return result

    # 문제 조건에 맞게 정렬
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    # print(data)


    for i in range(row_begin, row_end + 1):
        # print(data[i-1])
        # print(si(i))
        # print("*****")

        # row_begin - row_end 까지 S_i를 구함
        xor.append(si(i))
    # print(xor)
    answer = xor[0]
    # print(answer)

    # bitwise XOR 
    for i in range(1, len(xor)):
        answer = answer ^ xor[i]
    return answer
