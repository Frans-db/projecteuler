import math

num = 600851475143
for i in range(3, int(math.sqrt(num))):
    while num % i == 0 and num != 0:
        num = num / i
        print(i, num)  