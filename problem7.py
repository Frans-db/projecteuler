prime_amount = 3
i = 3
while prime_amount <= 10001:
    i += 2
    if any(i % j == 0 for j in range(3, i,2)):
        continue
    print(i, prime_amount)
    prime_amount += 1
    #i += 1
        
print(f'Prime amount {prime_amount}')