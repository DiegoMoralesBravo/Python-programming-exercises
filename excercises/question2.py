x = int(input())
total = 1
for i in range(x, -1):
    print(i)
    total += total * i
print(total)
