n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(str, input())))

cnt, hd = 0, 0
result = ''
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if arr[j][i] == 'T':
            t += 1
        elif arr[j][i] == 'A':
            a += 1
        elif arr[j][i] == 'G':
            g += 1
        elif arr[j][i] == 'C':
            c += 1
    if max(a,c,g,t) == a:
        result += 'A'
        hd += c + g +t
    elif max(a,c,g,t) == c:
        result += 'C'
        hd += a + g +t
    elif max(a,c,g,t) == g:
        result += 'G'
        hd += a + c +t
    elif max(a,c,g,t) == t:
        result += 'T'
        hd += c + g + a

print(result)
print(hd)

'''
아님 걍 입력받은 DNA들 전부 파이썬 데이터프레임에 떄려박고 .mode 갈기면 안되나?
TATGATAC 1
TAAGCTAC 1
AAAGATCC 2
TGAGATAC 1
TAAGATGT 2

TAAGATAC
7



import pandas as pd

n, m = map(int,input().split())
arr = []

#DNA들 리스트로 입력받고, M*N 데이터프레임으로 변환
for i in range(n):
    arr.append(list(map(str, input())))

arr_df = pd.DataFrame(arr)

#열별 최빈값
modes_string = ''

for column in arr_df.columns:
    mode = arr_df[column].mode().iloc[0]  # 이 줄은 구글링 했음
    modes_string += mode

print(modes_string)
'''