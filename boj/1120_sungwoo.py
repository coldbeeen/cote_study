a, b = input().split()

longer, shorter = (a,b) if len(a) > len(b) else (b,a)
len_l, len_s = len(longer), len(shorter)

diff = len(longer)
i = 0
while i < len_l - len_s + 1:  # shorter로 longer를 한칸씩 훑어보기

    diffTmp = 0
    for j in range(len_s):  # 각 요소를 다른지  검사
        if longer[i+j] != shorter[j]:
            diffTmp += 1

    if diffTmp < diff:  # min diff 갱신
        diff = diffTmp

    i += 1

print(diff)