# 1시간 31분

def solution(order):
    sub = []

    idx = 0
    # order의 길이만큼 수행하는데, 상자의 번호는 1번부터
    # 처음에는 상자번호가 안맞으면 스택에 넣었는데, if else가 너무 많아서 복잡해지고, 변수도 많이 써야돼서 애먹었음

    #  꺼내는 대로 넣어놓고, 번호가 맞으면 빼서 트럭에 싣고 idx+1(다음 순서)
    for num in range(1, len(order) + 1):
        sub.append(num)

        while sub and sub[-1] == order[idx]:
            sub.pop()
            idx += 1

    return idx
