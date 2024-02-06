import sys

input = sys.stdin.readline

string = input().strip()
target = input().strip()

cnt = 0
idx = 0
while idx <= len(string):
    compare = string[idx:idx+len(target)] #target길이만큼 잘라서 비교를 해보자
    
    if compare == target:
        cnt += 1
        idx += len(target) #중복되면 안되니까 skip
        continue
    
    idx += 1

print(cnt)