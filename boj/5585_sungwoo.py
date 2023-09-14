n = int(input())

coin = [500, 100, 50, 10, 5, 1]
change = 1000 - n
result = 0

for i in coin:
    num_coin = change // i
    change -= i * num_coin
    result += change // i

    if change == 0:
        break

print(result)