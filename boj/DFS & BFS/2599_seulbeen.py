# 감이 안와서 구글링했는데 애초에 DFS가 아니었음,, 그래도 풀었어야했는디
n= int(input())
school = []
check = True
for i in range(0, 3):
    x, y = map(int, input().split())
    school.append(x)
    school.append(y)

for i in range(0, school[0]+1):
    a = i
    d = school[0] - a
    e = school[5] - d
    b = school[2] - e
    c = school[1] - b
    f = school[4] - c
    
    if a >= 0 and b >= 0 and c >= 0 and d >=0 and e >= 0 and f >=0 :
        print(1)
        print(a, d)
        print(b, e)
        print(c, f)
        check = False
        break

if check:
    print(0)