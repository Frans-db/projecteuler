a = 1
b = 1
total = 0
while True:
    temp = b
    b = a + b
    a = temp
    if b > 4000000:
        break
    if b % 2 == 0:
        total += b
print(total)