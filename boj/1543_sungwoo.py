import sys
input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()

i = 0
doc_len = len(doc)
word_len = len(word)

result = 0

while i < doc_len:
    
    if doc[i: i+word_len] == word:
        result += 1
        i += word_len
        continue
    i += 1

print(result)