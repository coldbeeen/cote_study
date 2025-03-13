# 구글링...
result = []
def solution(s):
    for i in range(1, int(len(s) / 2) + 1):
        space = ""
        cnt = 1
        for j in range(0, len(s), i):
            if s[j : j + i] == s[j + i : j + i * 2]:
                cnt += 1
                target = s[j : j + i]
            elif cnt > 1:
                space += str(cnt) + target
                cnt = 1
            else:
                space += s[j : j + i]
        result.append(len(space))
    return 1 if len(s) == 1 else min(result)
