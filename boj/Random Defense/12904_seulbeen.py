import sys

input=sys.stdin.readline
s=input().rstrip()
t=list(input().rstrip())
# t=t[::-1]
# print(t)

while len(t)>=len(s):
    if t[-1]=='A':
        t.pop()
    else:
        t.pop()
        t=t[::-1]

    if len(t)==len(s):
        if t==list(s):
            print(1)
        else:
            print(0)
        break
