def solution(str1, str2):

    str1 = str1.upper()
    str2 = str2.upper()

    multi1 = []
    multi2 = []

    for i in range(1, len(str1)):
        tmp = str1[i - 1] + str1[i]
        if tmp.isalpha():
            multi1.append(tmp)
    for i in range(1, len(str2)):
        tmp = str2[i - 1] + str2[i]
        if tmp.isalpha():
            multi2.append(tmp)

    bis = []
    tmp = multi2.copy()
    for item in multi1:
        if item in tmp:
            tmp.remove(item)
            bis.append(item)
    un = len(multi1) + len(multi2) - len(bis)

    if un == 0:
        return 65536
    else:
        return int((len(bis) / un) * 65536)
