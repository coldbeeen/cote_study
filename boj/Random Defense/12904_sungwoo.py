s1, s2 = input(), input()

while len(s1) != len(s2):  # 두 문자열의 길이가 같아질 때까지
    if s2[-1] == 'A':  # 마지막 문자가 A라면 제거
        s2 = s2[:-1]
    else:  # 마지막 문자가 B라면 제거 후 reverse
        s2 = s2[:-1][::-1]

print(int(s1 == s2))  # 같다면 1, 다르면 0