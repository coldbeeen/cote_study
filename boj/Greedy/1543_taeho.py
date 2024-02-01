import sys
input = sys.stdin.readline

doc = input().strip()
find = input().strip()

find_split = doc.split(find) # 반복되는 find들 사이에 낑긴 놈들 뽑고

#print(find_split)
#print(len(find_split))

print(len(find_split) - 1) # 뽑힌 놈들 사이에 낑긴 find 개수니까 -1 해주면 됨