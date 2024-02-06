import sys

num = 1000 - int(sys.stdin.readline()) #거슬러줘야하는 돈 액수

cnt = 0

change = [500, 100, 50, 10, 5, 1]
idx = 0

while num > 0 :
    if num < change[idx] :
        while num < change[idx] :
            idx += 1
    num -= change[idx]
    cnt += 1

print(cnt)
