l, c = map(int, input().split())
alphabet_list = sorted(input().split())
vowel_list = ['a', 'e', 'i', 'o', 'u']

def search(idx, password):
    if len(password) == l:  # l개 알파벳으로 구성되었을 때 (return 되므로 l개를 초과하는 조합 생성 X)
        vowel_cnt, not_vowel_cnt = 0, 0
        for ch in password:
            if ch in vowel_list:
                vowel_cnt += 1
            else:
                not_vowel_cnt += 1

        if vowel_cnt >= 1 and not_vowel_cnt >= 2:  # 조건 확인 후 출력
            print(''.join(password))
        return  # 종료 (더이상 재귀 X)

    # idx는 조합 중인 상태에서 alphabet_list의 현재 인덱스 위치
    for i in range(idx, c):
        password.append(alphabet_list[i])
        search(i + 1, password)
        password.pop()

search(0, [])