#약 27분 소요

import sys

input = sys.stdin.readline

def is_vowel(char):
    vowel = ['a', 'e', 'i', 'o', 'u']

    if char in vowel:
        return True
    else:
        return False

while True:
    string = list(input().strip())

    if ''.join(string) == 'end':
        break

    vowel_flag = False #1번 규칙
    cnt_flag = False #2번 규칙
    same_flag = False #3번 규칙

    v_cnt = 0 #모음 카운트
    c_cnt = 0 #자음 카운트

    char = '?'

    for i in range(len(string)):
        if is_vowel(string[i]):
            vowel_flag = True #1번 규칙 만족

            v_cnt += 1
            c_cnt = 0
        else:
            c_cnt += 1
            v_cnt = 0
        
        if v_cnt == 3 or c_cnt >= 3: #2번 규칙 불만족
            cnt_flag = True
        
        if string[i] == char:
            if string[i] == 'e' or string[i] == 'o':
                pass
            else:
                same_flag = True #3번 규칙 불만족
        
        char = string[i] #규칙 3번 체크 용도 갱신
    
    if not vowel_flag or cnt_flag or same_flag:
        print(f"<{''.join(string)}> is not acceptable.")
    else:
        print(f"<{''.join(string)}> is acceptable.")