import sys

num = 1000 - int(sys.stdin.readline()) #거슬러줘야하는 돈 액수

cnt = 0

change = [500, 100, 50, 10, 5, 1] #리스트보단 튜플이 낫다. 엔 값이 변하면 안되기 때문
idx = 0

while num > 0 :
    if num < change[idx] :
        while num < change[idx] :
            idx += 1
    num -= change[idx]
    cnt += 1

print(cnt)

#while 문을 한번만 써서 해결할 수는 없었을까?

# 1중 반복문으로 풀 수 있었음 (태호, 성우)